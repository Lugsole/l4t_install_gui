pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'l4t_install_gui')
gnome = import('gnome')

gnome.compile_resources('l4t_install_gui',
  'l4t_install_gui.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'l4t_install_gui.in',
  output: 'l4t_install_gui',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

configure_file(
  input: 'config.py.in',
  output: 'config.py',
  configuration: conf,
  install: true,
  install_dir: moduledir
)

l4t_install_gui_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'MenuGroup.py',
  'MenuItem.py',
  'GenMenu.py',
]

install_data(l4t_install_gui_sources, install_dir: moduledir)
