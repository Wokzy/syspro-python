
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <string.h>


static double **matrix_new(size_t size) {
	double **res = calloc(sizeof(double*), size);
	for (size_t i = 0; i < size; i++) {
		res[i] = calloc(sizeof(double), size);
	}
	return res;
}

static double **matrix_copy(double **a, size_t size) {
	double **res = calloc(sizeof(double*), size);
	for (size_t i = 0; i < size; i++) {
		res[i] = calloc(sizeof(double), size);
		memcpy(res[i], a[i], sizeof(double)*size);
	}
	return res;
}

static void matrix_destroy(double **a, size_t size) {
	for (size_t i = 0; i < size; i++)
		free(a[i]);
	free(a);
}


static double **matrix_mul(double **a, double **b, size_t size) {
	double **res = matrix_new(size);

	for (size_t i = 0; i < size; i++)
		for (size_t j = 0; j < size; j++)
			for (size_t k = 0; k < size; k++)
				res[i][j] += a[i][k] * b[k][j];

	return res;
}

static double **matrix_pow(double **a, size_t size, size_t power) {
	if (power == 0)
		return matrix_new(size);

	double **res = matrix_copy(a, size);

	for (size_t rcx = 0; rcx < power - 1; rcx++) {
		double **cache = matrix_mul(a, res, size);
		matrix_destroy(res, size);
		res = cache;

	}
	return res;
}


static PyObject *foreign_matrix_power(PyObject *self, PyObject *args)
{
	PyObject *matrix;
	size_t matrix_size;
	size_t power;

	if (!PyArg_ParseTuple(args, "On", &matrix, &power))
		return NULL;

	Py_INCREF(matrix);
	matrix_size = PyObject_Length(matrix);
	// printf("power: %zu\n", power);

	PyObject *output = PyList_New(matrix_size);
	Py_INCREF(output);

	double **input_matrix = matrix_new(matrix_size);

	for (size_t i = 0; i < matrix_size; i++) {
		PyObject *vector = PyList_GetItem(matrix, i);
		Py_INCREF(vector);
		for (size_t j = 0; j < matrix_size; j++) {
			PyObject *pyfloat = PyList_GetItem(vector, j);
			Py_INCREF(pyfloat);
			input_matrix[i][j] = PyFloat_AsDouble(pyfloat);
			// printf("%lf\n", input_matrix[i][j]);
			Py_DECREF(pyfloat);
		}
		Py_DECREF(vector);
	}

	double **res = matrix_pow(input_matrix, matrix_size, power);
	for (size_t i = 0; i < matrix_size; i++) {
		PyObject *out_vector = PyList_New(matrix_size);
		Py_INCREF(out_vector);
		for (size_t j = 0; j < matrix_size; j++)
			PyList_SetItem(out_vector, j, PyFloat_FromDouble(res[i][j]));
		PyList_SetItem(output, i, out_vector);
		Py_DECREF(out_vector);
	}

	matrix_destroy(input_matrix, matrix_size);
	matrix_destroy(res, matrix_size);
	Py_DECREF(output);
	Py_DECREF(matrix);
	return output;
}

static PyMethodDef ForeignMethods[] = {
	{"foreign_matrix_power",
	foreign_matrix_power, METH_VARARGS,
	"Matrix exponentiation"
	},
	{NULL, NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef foreignmodule = {
	PyModuleDef_HEAD_INIT,
	"foreign", /* name of module */
	NULL, /* module documentation, may be NULL */
	-1, /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
	ForeignMethods
};

PyMODINIT_FUNC PyInit_foreign(void)
{
	return PyModule_Create(&foreignmodule);
}
