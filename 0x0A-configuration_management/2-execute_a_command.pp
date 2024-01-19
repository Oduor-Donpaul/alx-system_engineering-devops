#Kill the proces killnow
exec { 'pkill':
  command  => 'pkill killnow';
  provider  => 'shell';
}
