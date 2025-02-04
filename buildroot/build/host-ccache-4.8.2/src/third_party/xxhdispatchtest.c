#include "xxh_x86dispatch.c"

int main()
{
  XXH3_64bits_dispatch("foo", 3);
  return 1;
}
