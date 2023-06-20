CC = gcc
CFLAGS_COMPILE = -fPIC
CFLAGS_DEBUG = -shared -o

BIN_DIR = bin/
SRC_DIR = src/

SRC_C := $(shell find $(SRC_DIR) -type f -name "*.c")
SRC = $(SRC_C)
OBJ = $(SRC:$(SRC_DIR)%.c=$(BUILD_DIR)%.o)
SO = $(OBJ:.c=.o)

.PHONY: bin clean

$(BIN_DIR)TP_miniglibc: $(OBJ) $(SO)
	@mkdir -p $(dir $@)
	@$(CC) $(CFLAGS_DEBUG) $@ $(CFLAGS_COMPILE)

clean:
	rm -r $(BIN_DIR)