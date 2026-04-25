; ModuleID = "js_compiler"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = bitcast [4 x i8]* @"fstr_1" to i8*
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 0)
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr_1" = internal constant [4 x i8] c"%d\0a\00"