/* This file has been generated by the Hex-Rays decompiler.
   Copyright (c) 2009 Hex-Rays <info@hex-rays.com>

   Detected compiler: GNU C++
*/

#include <defs.h>


//-------------------------------------------------------------------------
// Data declarations

extern _UNKNOWN start; // weak
extern char format[]; // idb
extern char a_[2]; // weak
extern char aSorryWeAreNotA[53]; // weak
extern char aDoYouWantToLea[39]; // weak
extern char aBye[6]; // weak
extern int (*off_8049F08[2])(); // weak
extern int (*off_8049F0C)(); // weak
extern char byte_804A040; // weak
extern int dword_804A044; // weak
extern char byte_804A060; // weak
extern char byte_804A061; // weak
extern char byte_804A062; // weak
extern char byte_804A063; // weak
// extern _UNKNOWN _gmon_start__; weak

//-------------------------------------------------------------------------
// Function declarations

int __cdecl init_proc();
time_t time(time_t *timer);
unsigned int sleep(unsigned int seconds);
unsigned int alarm(unsigned int seconds);
int __fastcall __stack_chk_fail(_DWORD, _DWORD); // weak
int __gmon_start__(void); // weak
size_t strftime(char *s, size_t maxsize, const char *format, const struct tm *tp);
struct tm *localtime(const time_t *timer);
int sprintf(char *s, const char *format, ...);
void __cdecl sub_8048490();
signed int __cdecl sub_80484A0();
void __cdecl sub_8048510();
int __cdecl sub_8048530();
int __cdecl sub_804855D(int a1, const char *a2);
int __cdecl sub_80485CE();
int __cdecl sub_80486B1();
int __cdecl sub_8048700();
int __cdecl sub_80487B0(void *addr, int); // idb
int __cdecl sub_80487E4(const void *addr); // idb
int __cdecl sub_8048810(int a1, int a2, int a3);
void __cdecl term_proc();


//----- (0804839C) --------------------------------------------------------
int __cdecl init_proc()
{
  int result; // eax@1

  result = (int)&_gmon_start__;
  if ( &_gmon_start__ )
    result = __gmon_start__();
  return result;
}
// 8048410: using guessed type int __gmon_start__(void);

//----- (08048460) --------------------------------------------------------
#error "8048463: positive sp value has been found (funcsize=2)"

//----- (08048490) --------------------------------------------------------
void __cdecl sub_8048490()
{
  ;
}

//----- (080484A0) --------------------------------------------------------
signed int __cdecl sub_80484A0()
{
  return 3;
}
// 80484A0: could not find valid save-restore pair for ebp

//----- (08048510) --------------------------------------------------------
void __cdecl sub_8048510()
{
  if ( !byte_804A040 )
  {
    sub_80484A0();
    byte_804A040 = 1;
  }
  __asm { rep retn }
}
// 804A040: using guessed type char byte_804A040;

//----- (08048530) --------------------------------------------------------
int __cdecl sub_8048530()
{
  return 0;
}
// 8048530: could not find valid save-restore pair for ebp

//----- (0804855D) --------------------------------------------------------
int __cdecl sub_804855D(int a1, const char *a2)
{
  int result; // eax@1
  int v3; // edx@1
  int v4; // ecx@1
  char addr; // [sp+2Ch] [bp-8Ch]@1
  int v6; // [sp+ACh] [bp-Ch]@1

  v6 = *MK_FP(__GS__, 20);
  sprintf(&addr, a2, a1, &byte_804A060);
  sub_80487E4(&addr);
  result = *MK_FP(__GS__, 20) ^ v6;
  if ( *MK_FP(__GS__, 20) != v6 )
    __stack_chk_fail(v4, v3);
  return result;
}
// 8048400: using guessed type int __fastcall __stack_chk_fail(_DWORD, _DWORD);
// 804A060: using guessed type char byte_804A060;

//----- (080485CE) --------------------------------------------------------
int __cdecl sub_80485CE()
{
  int v0; // edx@2
  int v1; // ecx@2
  int result; // eax@4
  time_t timer; // [sp+14h] [bp-84h]@1
  struct tm *tp; // [sp+18h] [bp-80h]@1
  int v5; // [sp+1Ch] [bp-7Ch]@1
  int v6; // [sp+20h] [bp-78h]@1
  int v7; // [sp+24h] [bp-74h]@1
  int v8; // [sp+28h] [bp-70h]@1
  int v9; // [sp+2Ch] [bp-6Ch]@1
  int v10; // [sp+30h] [bp-68h]@1
  int v11; // [sp+34h] [bp-64h]@1
  int v12; // [sp+38h] [bp-60h]@1
  char s; // [sp+3Ch] [bp-5Ch]@1
  int v14; // [sp+8Ch] [bp-Ch]@1

  v14 = *MK_FP(__GS__, 20);
  v5 = 538976288;
  v6 = 538976288;
  v7 = 607266080;
  v8 = 2675;
  v9 = 1931834149;
  v10 = 10;
  v11 = 0;
  v12 = 0;
  time(&timer);
  tp = localtime(&timer);
  strftime(&s, 0x50u, "%H:%M:%S ", tp);
  if ( timer == dword_804A044 )
  {
    sub_804855D((int)&s, (const char *)&v5);
  }
  else
  {
    dword_804A044 = timer;
    sub_804855D((int)&s, (const char *)&v9);
  }
  result = *MK_FP(__GS__, 20) ^ v14;
  if ( *MK_FP(__GS__, 20) != v14 )
    __stack_chk_fail(v1, v0);
  return result;
}
// 8048400: using guessed type int __fastcall __stack_chk_fail(_DWORD, _DWORD);
// 804A044: using guessed type int dword_804A044;

//----- (080486B1) --------------------------------------------------------
int __cdecl sub_80486B1()
{
  int result; // eax@4

  while ( 1 )
  {
    sub_80487B0(&byte_804A060, 1024);
    if ( byte_804A060 == 69 )
    {
      if ( byte_804A061 == 78 )
      {
        if ( byte_804A062 == 68 )
        {
          result = (unsigned __int8)byte_804A063;
          if ( !byte_804A063 )
            break;
        }
      }
    }
    sub_80485CE();
  }
  return result;
}
// 804A060: using guessed type char byte_804A060;
// 804A061: using guessed type char byte_804A061;
// 804A062: using guessed type char byte_804A062;
// 804A063: using guessed type char byte_804A063;

//----- (08048700) --------------------------------------------------------
int __cdecl sub_8048700()
{
  int result; // eax@5
  int v1; // ecx@5
  signed int i; // [sp+14h] [bp-Ch]@1
  char v3; // [sp+18h] [bp-8h]@4
  int v4; // [sp+1Ch] [bp-4h]@1

  v4 = *MK_FP(__GS__, 20);
  alarm(0x1Eu);
  for ( i = 0; i <= 2; ++i )
  {
    sub_80487E4(".");
    sleep(1u);
  }
  sub_80487E4("Sorry, we are not able to take your call right now.\n");
  sub_80487E4("Do you want to leave a message (y/n)? ");
  sub_80487B0(&v3, 4);
  if ( v3 == 121 )
    result = sub_80486B1();
  else
    result = sub_80487E4("Bye!\n");
  if ( *MK_FP(__GS__, 20) != v4 )
    __stack_chk_fail(v1, *MK_FP(__GS__, 20) ^ v4);
  return result;
}
// 8048400: using guessed type int __fastcall __stack_chk_fail(_DWORD, _DWORD);

//----- (080487B0) --------------------------------------------------------
int __cdecl sub_80487B0(void *addr, int a2)
{
  size_t v2; // edx@1
  void *v3; // ecx@1
  int v4; // esi@1
  int result; // eax@3

  v3 = addr;
  v2 = 1;
  v4 = a2;
  while ( 1 )
  {
    --v4;
    if ( !v4 )
      break;
    result = sys_read(0, v3, v2);
    if ( *(_BYTE *)v3 == 10 )
      break;
    v3 = (char *)v3 + 1;
  }
  *(_BYTE *)v3 = 0;
  return result;
}

//----- (080487E4) --------------------------------------------------------
int __cdecl sub_80487E4(const void *addr)
{
  size_t v1; // edx@1
  const void *v2; // ecx@1
  int result; // eax@3
  int v4; // ecx@3

  v2 = addr;
  v1 = 1;
  while ( *(_BYTE *)v2 )
  {
    result = sys_write(1, v2, v1);
    v2 = (const void *)(v4 + 1);
  }
  return result;
}

//----- (08048810) --------------------------------------------------------
int __cdecl sub_8048810(int a1, int a2, int a3)
{
  int result; // eax@1
  int v4; // edi@1
  signed int v5; // esi@1

  v4 = 0;
  init_proc();
  result = (int)off_8049F08;
  v5 = (signed int)((char *)&off_8049F0C - (char *)off_8049F08) >> 2;
  if ( v5 )
  {
    do
      result = ((int (__cdecl *)(int, int, int))off_8049F08[v4++])(a1, a2, a3);
    while ( v4 != v5 );
  }
  return result;
}
// 8049F08: using guessed type int (*off_8049F08[2])();
// 8049F0C: using guessed type int (*off_8049F0C)();

//----- (08048884) --------------------------------------------------------
void __cdecl term_proc()
{
  ;
}

#error "There were 1 decompilation failure(s) on 14 function(s)"
