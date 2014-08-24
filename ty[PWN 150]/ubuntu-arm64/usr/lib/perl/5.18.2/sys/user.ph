require '_h2ph_pre.ph';

no warnings qw(redefine misc);

unless(defined(&_SYS_USER_H)) {
    eval 'sub _SYS_USER_H () {1;}' unless defined(&_SYS_USER_H);
    require 'asm/ptrace.ph';
    undef(&PTRACE_GET_THREAD_AREA) if defined(&PTRACE_GET_THREAD_AREA);
    undef(&PTRACE_GETHBPREGS) if defined(&PTRACE_GETHBPREGS);
    undef(&PTRACE_SETHBPREGS) if defined(&PTRACE_SETHBPREGS);
}
1;
