; ModuleID = "js_compiler"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = mul i32 6, 6
  %".3" = mul i32 8, 8
  %".4" = mul i32 10, 10
  %".5" = add i32 %".2", %".3"
  %".6" = bitcast [4 x i8]* @"fstr_1" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".2")
  %".8" = bitcast [4 x i8]* @"fstr_2" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %".3")
  %".10" = bitcast [4 x i8]* @"fstr_3" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i32 %".4")
  %".12" = bitcast [4 x i8]* @"fstr_4" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i32 %".5")
  %".14" = mul i32 6, 6
  %".15" = mul i32 8, 8
  %".16" = add i32 %".14", %".15"
  %".17" = bitcast [4 x i8]* @"fstr_5" to i8*
  %".18" = call i32 (i8*, ...) @"printf"(i8* %".17", i32 %".16")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr_1" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_2" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_3" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_4" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_5" = internal constant [4 x i8] c"%d\0a\00"