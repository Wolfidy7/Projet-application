CC = gcc
CFLAGS_COMPILE = -c -fPIC -Isrc
CFLAGS_DEBUG = -shared
CFLAGS = $(CFLAGS_COMPILE) $(CFLAGS_DEBUG)

LD = gcc
LDFLAGS =

BIN_DIR = bin/
SRC_DIR = src/
BUILD_DIR = build/

SRC_C := $(shell find $(SRC_DIR) -type f -name "*.c")
SRC = $(SRC_C)
OBJ = $(SRC:$(SRC_DIR)%.c=$(BUILD_DIR)%.o)
SO = $(OBJ:.o=.so)

.PHONY: bin clean

bin: $(BIN_DIR)TP_miniglibc

$(BIN_DIR)TP_miniglibc: $(OBJ) $(SO)
	@$(LD) $^ -o $@ $(LDFLAGS)

$(BUILD_DIR)%.so: $(BUILD_DIR)%.c
	@mkdir -p $(dir $@)
	@$(LD) $(CFLAGS_DEBUG) $< -o $@

clean:
	rm -r $(BUILD_DIR)
	rm -r $(BIN_DIR)

-include $(SO)
