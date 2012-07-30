#ifndef _CGROUP_H_
#define _CGROUP_H_

#include <libcgroup.h>
#include "types.h"

#define CT_BASE_STRING "/vz/"
#define CT_MAX_STR_SIZE STR_SIZE

#define veid_to_name(buf, veid) snprintf(buf, CT_MAX_STR_SIZE, "%s%d", \
				CT_BASE_STRING, veid)

int container_is_running(envid_t veid);
int destroy_container(envid_t veid);
int create_container(envid_t veid);
int container_add_task(envid_t veid);

static inline const char *container_error(int ret)
{
	return cgroup_strerror(ret);
}

int container_init(void);
#endif /* _CGROUP_H_ */