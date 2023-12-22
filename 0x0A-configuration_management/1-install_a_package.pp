# Downloads the package flask using pip
package {'flask':
	provider => 'pip3',
  name => 'flask==2.1.0'
}
