/*
 *  Copyright (C) 2000-2008, Parallels, Inc. All rights reserved.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */
#ifndef _VZCTL_H_
#define _VZCTL_H_

typedef enum {
	ACTION_CREATE		= 1,
	ACTION_DESTROY,
	ACTION_MOUNT,
	ACTION_UMOUNT,
	ACTION_START,
	ACTION_STOP,
	ACTION_RESTART,
	ACTION_SET,
	ACTION_STATUS,
	ACTION_EXEC,
	ACTION_EXEC2,
	ACTION_EXEC3,
	ACTION_ENTER,
	ACTION_RUNSCRIPT,
	ACTION_CUSTOM,
	ACTION_CHKPNT,
	ACTION_RESTORE,
	ACTION_QUOTAON,
	ACTION_QUOTAOFF,
	ACTION_QUOTAINIT
} act_t;

/* default cpu units values */
#define LHTCPUUNITS		250
#define UNLCPUUNITS		1000
#define HNCPUUNITS		1000

/* setmode flags */
enum {
	SET_NONE = 0,
	SET_IGNORE,
	SET_RESTART,
};

#endif
