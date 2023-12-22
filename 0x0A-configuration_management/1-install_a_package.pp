# Downloads the package flask using pip3
package {'Flask':
  provider        => 'pip3',
  name            => 'flask==2.1.0',
  install_options => 'install'
}
