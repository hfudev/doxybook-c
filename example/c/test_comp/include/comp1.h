/**
 * @file comp1.h
 * @brief This is a test file for comp1
 *
 * To use this driver:
 * - include this file in your project
 * - @ref print() is a function that prints "Hello World!"
 */

/**
 * @brief print function
 *
 */
void print(void);

/**
 * @brief print the added result
 *
 * @param a aaa
 * @param b bbb
 */
void add(comp1 a, comp1 b);


/**
 * @brief THIS IS TEST_FOO VARIABLE!
 *
 */
#define TEST_FOO 111;


/**
 * @brief struct comp
 *
 */
struct comp1
{
    /**
     * @brief ??? foo?
     *
     */
    int foo;
    int bar;
};


/**
 * @brief typedef int for comp
 *
 */
typedef int comp1_int;


/**
 * @brief it's a union!!!
 *
 */
union union_comp1
{
    comp1 a;
    comp1 b;
};
