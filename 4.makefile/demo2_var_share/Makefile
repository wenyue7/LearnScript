SUBDIRS := subdir1 subdir2 subdir3

include common.mk

EX_VAL := ex_share_val
EX_VAL += ex_share_val2
# 可以多次导出，即可以每次修改都导出一次，或者需要的时候导出一次
# 实际测试发现即便先导出，也可以显示导出之后，重新修改的值
export EX_VAL
# 已经export过的变量，也可以通过 unexport 取消
# unexport EX_VAL

.PHONY: all clean $(SUBDIRS)

all: $(SUBDIRS)

$(SUBDIRS):
	@$(MAKE) -C $@

clean:
	@for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir clean; \
	done

