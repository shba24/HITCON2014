require '_h2ph_pre.ph';

no warnings qw(redefine misc);

unless(defined(&_BITS_PTHREADTYPES_H)) {
    eval 'sub _BITS_PTHREADTYPES_H () {1;}' unless defined(&_BITS_PTHREADTYPES_H);
    require 'endian.ph';
    eval 'sub __SIZEOF_PTHREAD_ATTR_T () {64;}' unless defined(&__SIZEOF_PTHREAD_ATTR_T);
    eval 'sub __SIZEOF_PTHREAD_MUTEX_T () {48;}' unless defined(&__SIZEOF_PTHREAD_MUTEX_T);
    eval 'sub __SIZEOF_PTHREAD_MUTEXATTR_T () {8;}' unless defined(&__SIZEOF_PTHREAD_MUTEXATTR_T);
    eval 'sub __SIZEOF_PTHREAD_COND_T () {48;}' unless defined(&__SIZEOF_PTHREAD_COND_T);
    eval 'sub __SIZEOF_PTHREAD_COND_COMPAT_T () {48;}' unless defined(&__SIZEOF_PTHREAD_COND_COMPAT_T);
    eval 'sub __SIZEOF_PTHREAD_CONDATTR_T () {8;}' unless defined(&__SIZEOF_PTHREAD_CONDATTR_T);
    eval 'sub __SIZEOF_PTHREAD_RWLOCK_T () {56;}' unless defined(&__SIZEOF_PTHREAD_RWLOCK_T);
    eval 'sub __SIZEOF_PTHREAD_RWLOCKATTR_T () {8;}' unless defined(&__SIZEOF_PTHREAD_RWLOCKATTR_T);
    eval 'sub __SIZEOF_PTHREAD_BARRIER_T () {32;}' unless defined(&__SIZEOF_PTHREAD_BARRIER_T);
    eval 'sub __SIZEOF_PTHREAD_BARRIERATTR_T () {8;}' unless defined(&__SIZEOF_PTHREAD_BARRIERATTR_T);
    unless(defined(&__have_pthread_attr_t)) {
	eval 'sub __have_pthread_attr_t1 () {1;}' unless defined(&__have_pthread_attr_t1);
    }
    eval 'sub __PTHREAD_MUTEX_HAVE_PREV () {1;}' unless defined(&__PTHREAD_MUTEX_HAVE_PREV);
    if(defined (&__USE_UNIX98) || defined (&__USE_XOPEN2K)) {
    }
    if(defined(&__USE_XOPEN2K)) {
    }
}
1;
