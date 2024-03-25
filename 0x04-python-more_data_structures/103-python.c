#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list object
 */
void print_python_list(PyObject *p)
{
    long int size = PyList_Size(p);
    int alloc = ((PyListObject *)p)->allocated;
    PyTypeObject *type;
    PyObject *item;
    printf("[*] Python list info\n");
    if (PyList_Check(p)) {
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %d\n", alloc);
        for (int i = 0; i < size; i++) {
            item = PyList_GetItem(p, i);
            type = item->ob_type;
            printf("Element %d: %s\n", i, type->tp_name);
            if (PyBytes_Check(item)) {
                print_python_bytes(item);
            }
        }
    } else {
        printf("  [ERROR] Invalid List Object\n");
    }
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size;
    char *trying_str = NULL;
    printf("[.] bytes object info\n");
    if (PyBytes_Check(p)) {
        PyBytes_AsStringAndSize(p, &trying_str, &size);
        printf("  size: %zd\n", size);
        printf("  trying string: %s\n", trying_str);
        printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
        for (int i = 0; i < (size < 10 ? size + 1 : 10) && i < size; i++) {
            printf(" %02hhx", trying_str[i]);
        }
        printf("\n");
    } else {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}
