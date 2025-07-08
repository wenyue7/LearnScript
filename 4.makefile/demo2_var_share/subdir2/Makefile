include ../common.mk

# 🔁 这里进行覆盖
CFLAGS := -g -DDEBUG
FOO := subdir1_custom_value
# 这里修改无效，因为 FIX_VAL 在 common.mk 中被 override 修饰
FIX_VAL := subdir2_custom_value

.PHONY: all clean

all:
	@echo "In subdir2:"
	@echo "Compiler: $(CC)"
	@echo "Flags:    $(CFLAGS)"
	@echo "FOO var:  $(FOO)"
	@echo "FIX var:  $(FIX_VAL)"

clean:
	@echo "Cleaning subdir2"

