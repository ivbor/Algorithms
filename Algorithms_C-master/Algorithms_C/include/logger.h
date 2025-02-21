#ifndef logger
#define logger

typedef enum {
    LOG_DEBUG,
    LOG_INFO,
    LOG_WARN,
    LOG_ERROR,
    LOG_FATAL
} log_level_t;

int set_log_level(log_level_t level);
void rotate_logs();
void check_log_rotation();
void log_message(log_level_t level, char* message);

#endif
