include ../common.mk

# 由于每个 make -C subdirX 是一个独立的子进程
# 因此，subdir2中修改的变量，不会作用于subdir3

.PHONY: all clean

all:
	@echo "In subdir3:"
	@echo "Compiler: $(CC)"
	@echo "Flags:    $(CFLAGS)"
	@echo "FOO var:  $(FOO)"
	@echo "FIX var:  $(FIX_VAL)"

clean:
	@echo "Cleaning subdir3"

