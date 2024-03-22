# Wagtail Waffle

Wagtail Waffle is a Django application designed to seamlessly integrate Django Waffle's feature flag capabilities with the Wagtail admin interface. This allows Wagtail users to manage feature flags directly from the Wagtail admin, making it easier to control the rollout of new features and functionality within Wagtail-based projects.

## Features

- **Wagtail Integration**: Directly manage Django Waffle flags, switches, and samples from the Wagtail admin.
- **User-Friendly Interface**: Leverages Wagtail's intuitive UI to provide a straightforward experience for managing feature flags.
- **Permissions Control**: Utilize Wagtail's permissions system to control access to feature flag management.

## Quick start

1. Install the package

   ```python
   pip install wagtail-waffle
   ```

2. Add "wagtail_waffle" to your `INSTALLED_APPS`:

   ```python
   INSTALLED_APPS = [
       ...,
       "wagtail_waffle",
   ]
   ```

After installation, you will find a new section in the Wagtail admin under the name "Features" for managing feature flags, switches, and samples. Here, you can create, update, and delete feature flags as needed for your project.

## Contributing

Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django Waffle for providing the feature flag framework.
- Wagtail for the powerful CMS capabilities.
