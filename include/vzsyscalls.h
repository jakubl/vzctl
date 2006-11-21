/*
 *  Copyright (C) 2000-2006 SWsoft. All rights reserved.
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
#ifndef _VZSYSCALLS_H_
#define _VZSYSCALLS_H_

#include <sys/syscall.h>

#ifdef __ia64__
#define __NR_fairsched_vcpus	1499
#define __NR_fairsched_chwt	1502
#define __NR_fairsched_rate	1504
#define __NR_setluid		1506
#define __NR_setublimit		1507
#elif __x86_64__
#define __NR_fairsched_vcpus	499
#define __NR_setluid		501
#define __NR_setublimit		502
#define __NR_fairsched_chwt	506
#define __NR_fairsched_rate	508
#elif __powerpc__
#define __NR_fairsched_chwt	402
#define __NR_fairsched_rate	404
#define __NR_fairsched_vcpus	405
#define __NR_setluid		411
#define __NR_setublimit		412
#elif defined(__i386__) || defined(__sparc__)
#define __NR_fairsched_chwt	502
#define __NR_fairsched_rate	504
#define __NR_fairsched_vcpus	505
#define __NR_setluid		511
#define __NR_setublimit		512
#else
#error "no syscall for this arch"
#endif

#endif