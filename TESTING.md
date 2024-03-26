# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| about | about.html | ![screenshot](documentation/testing/html-about.png) | |
| bag | bag.html | ![screenshot](documentation/testing/html-bag.png) | |
| checkout | checkout.html | ![screenshot](documentation/testing/html-checkout.png) | |
| checkout | checkout_success.html | ![screenshot](documentation/testing/html-checkout_success.png) | |
| home | index.html | ![screenshot](documentation/testing/html-home.png) | |
| profiles | profile.html | ![screenshot](documentation/testing/html-profile.png) | |
| records | add_record.html | ![screenshot](documentation/testing/html-add_record.png) | |
| records | edit_record.html | ![screenshot](documentation/testing/html-edit.png) | |
| records | record_detail.html | ![screenshot](documentation/testing/html-details.png) | |
| records | records.html | ![screenshot](documentation/testing/html-records.png) | |
| templates | 404.html | ![screenshot](documentation/testing/html-404.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | checkout.css | ![screenshot](documentation/testing/css-checkout.png) | |
| profiles | profile.css | ![screenshot](documentation/testing/css-profiles.png) | |
| static | base.css | ![screenshot](documentation/testing/css-home.png) | |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | stripe_elements.js | ![screenshot](documentation/testing/validation/js-stripe.png) | |
| profiles | countryfield.js | ![screenshot](documentation/testing/validation/js-countryfield.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| about | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/about/urls.py) | ![screenshot](documentation/testing/validation/pep8-about-urls.png) | |
| about | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/about/views.py) | ![screenshot](documentation/testing/validation/pep8-about-views.png) | |

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| bag | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/bag/contexts.py) | ![screenshot](documentation/testing/validation/pep8-bag-contexts.png) | |
| bag | bag_tools.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/bag/templatetags/bag_tools.py) | ![screenshot](documentation/testing/validation/pep8-bag-bagtools.png) | |
| bag | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/bag/urls.py) | ![screenshot](documentation/testing/validation/pep8-bag-url.png) | |
| bag | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/bag/views.py) | ![screenshot](documentation/testing/validation/pep8-bag-views.png) | |

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| checkout | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/admin.py) | ![screenshot](documentation/testing/validation/pep8-checkout-admin.png) | |
| checkout | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/forms.py) | ![screenshot](documentation/testing/validation/pep8-checkout-forms.png) | |
| checkout | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/models.py) | ![screenshot](documentation/testing/validation/pep8-checkout-models.png) | |
| checkout | signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/signals.py) | ![screenshot](documentation/testing/validation/pep8-checkout-signals.png) | |
| checkout | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/urls.py) | ![screenshot](documentation/testing/validation/pep8-checkout-urls.png) | |
| checkout | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/views.py) | ![screenshot](documentation/testing/validation/pep8-checkout-views.png) | |
| checkout | webhook_handler.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/webhook_handler.py) | ![screenshot](documentation/testing/validation/pep8-checkout-whh.png) | |
| checkout | webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/webhooks.py) | ![screenshot](documentation/testing/validation/pep8-checkout-wh.png) | |

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| contact | context_processors.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/contact/context_processors.py) | ![screenshot](documentation/testing/validation/pep8-contact-context.png) | |
| contact | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/contact/forms.py) | ![screenshot](documentation/testing/validation/pep8-contact-forms.png) | |
| contact | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/contact/models.py) | ![screenshot](documentation/testing/validation/pep8-contact-models.png) | |
| contact | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/contact/urls.py) | ![screenshot](documentation/testing/validation/pep8-contact-urls.png) | |
| contact | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/contact/views.py) | ![screenshot](documentation/testing/validation/pep8-contact-views.png) | |


| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| faq | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/faq/admin.py) | ![screenshot](documentation/testing/validation/pep8-faq-admin.png) | |
| faq | context_processors.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/faq/context_processors.py) | ![screenshot](documentation/testing/validation/pep8-faq-context.png) | |
| faq | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/faq/models.py) | ![screenshot](documentation/testing/validation/pep8-faq-models.png) | |
| faq | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/faq/urls.py) | ![screenshot](documentation/testing/validation/pep8-faq-urls.png) | |
| faq | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/faq/views.py) | ![screenshot](documentation/testing/validation/pep8-faq-views.png) | |

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/home/urls.py) | ![screenshot](documentation/testing/validation/pep8-home-urls.png) | |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/home/views.py) | ![screenshot](documentation/testing/validation/pep8-home-views.png) | |

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| newsletter | content_processor.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/newsletter/content_processor.py) | ![screenshot](documentation/testing/validation/pep8-newsletter-context.png) | |
| newsletter | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/newsletter/forms.py) | ![screenshot](documentation/testing/validation/pep8-newsletter-forms.png) | |
| newsletter | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/newsletter/models.py) | ![screenshot](documentation/testing/validation/pep8-newsletter-models.png) | |
| newsletter | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/newsletter/urls.py) | ![screenshot](documentation/testing/validation/pep8-newsletter-urls.png) | |
| newsletter | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/newsletter/views.py) | ![screenshot](documentation/testing/validation/pep8-newsletter-views.png) | |

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| profiles | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/profiles/forms.py) | ![screenshot](documentation/testing/validation/pep8-profiles-forms.png) | |
| profiles | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/profiles/models.py) | ![screenshot](documentation/testing/validation/pep8-profiles-models.png) | |
| profiles | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/profiles/urls.py) | ![screenshot](documentation/testing/validation/pep8-profiles-urls.png) | |
| profiles | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/profiles/views.py) | ![screenshot](documentation/testing/validation/pep8-profiles-views.png) | |

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| records | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/records/admin.py) | ![screenshot](documentation/testing/validation/pep8-records-admin.png) | |
| records | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/records/forms.py) | ![screenshot](documentation/testing/validation/pep8-records-forms.png) | |
| records | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/records/models.py) | ![screenshot](documentation/testing/validation/pep8-records-models.png) | |
| records | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/records/urls.py) | ![screenshot](documentation/testing/validation/pep8-records-urls.png) | |
| records | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/records/views.py) | ![screenshot](documentation/testing/validation/pep8-records-views.png) | |
| records | widgets.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/records/widgets.py) | ![screenshot](documentation/testing/validation/pep8-records-widgets.png) | |

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| tonality | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/tonality/urls.py) | ![screenshot](documentation/testing/validation/pep8-tonality-urls.png) | |
|  | custom_storages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/custom_storages.py) | ![screenshot](documentation/testing/validation/pep8-customstorage.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-about.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-etc.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-about.png) | ![screenshot](documentation/browsers/browser-firefox-contact.png) | ![screenshot](documentation/browsers/browser-firefox-etc.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser-edge-home.png) | ![screenshot](documentation/browsers/browser-edge-about.png) | ![screenshot](documentation/browsers/browser-chrome-edge.png) | ![screenshot](documentation/browsers/browser-edge-etc.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/browser-safari-home.png) | ![screenshot](documentation/browsers/browser-safari-about.png) | ![screenshot](documentation/browsers/browser-safari-contact.png) | ![screenshot](documentation/browsers/browser-safari-etc.png) | Minor CSS differences |
| Brave | ![screenshot](documentation/browsers/browser-brave-home.png) | ![screenshot](documentation/browsers/browser-brave-about.png) | ![screenshot](documentation/browsers/browser-brave-contact.png) | ![screenshot](documentation/browsers/browser-brave-etc.png) | Works as expected |
| Opera | ![screenshot](documentation/browsers/browser-opera-home.png) | ![screenshot](documentation/browsers/browser-opera-about.png) | ![screenshot](documentation/browsers/browser-opera-contact.png) | ![screenshot](documentation/browsers/browser-opera-etc.png) | Minor differences |
| repeat for any other tested browsers | x | x | x | x | x |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | Records | Details | Bag | Checkout | Checkout2 | Edit | Add | Sign in | Order | Faq |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile Small | ![screenshot](documentation/testing/responsive/home-mobile-small.png) | ![screenshot](documentation/testing/responsive/about-mobile-small.png) | ![screenshot](documentation/testing/responsive/contact-mobile-small.png) | ![screenshot](documentation/testing/responsive/records-mobile-small.png) | ![screenshot](documentation/testing/responsive/detail-mobile-small.png) | ![screenshot](documentation/testing/responsive/bag-mobile-small.png) | ![screenshot](documentation/testing/responsive/checkout-mobile-small.png) | ![screenshot](documentation/testing/responsive/checkout2-mobile-small.png) | ![screenshot](documentation/testing/responsive/edit-mobile-small.png) | ![screenshot](documentation/testing/responsive/add-mobile-small.png) | ![screenshot](documentation/testing/responsive/signin-mobile-small.png) | ![screenshot](documentation/testing/responsive/order-mobile-small.png) | ![screenshot](documentation/testing/responsive/faq-mobile-small.png) |
| Mobile Medium | ![screenshot](documentation/testing/responsive/home-mobile-medium.png) | ![screenshot](documentation/testing/responsive/about-mobile-medium.png) | ![screenshot](documentation/testing/responsive/contact-mobile-medium.png) | ![screenshot](documentation/testing/responsive/records-mobile-medium.png) | ![screenshot](documentation/testing/responsive/detail-mobile-medium.png) | ![screenshot](documentation/testing/responsive/bag-mobile-medium.png) | ![screenshot](documentation/testing/responsive/checkout-mobile-medium.png) | ![screenshot](documentation/testing/responsive/checkout2-mobile-medium.png) | ![screenshot](documentation/testing/responsive/edit-mobile-medium.png) | ![screenshot](documentation/testing/responsive/add-mobile-medium.png) | ![screenshot](documentation/testing/responsive/signin-mobile-medium.png) | ![screenshot](documentation/testing/responsive/order-mobile-medium.png) | ![screenshot](documentation/testing/responsive/faq-mobile-medium.png) |
| Mobile Large | ![screenshot](documentation/testing/responsive/home-mobile-large.png) | ![screenshot](documentation/testing/responsive/about-mobile-large.png) | ![screenshot](documentation/testing/responsive/contact-mobile-large.png) | ![screenshot](documentation/testing/responsive/records-mobile-large.png) | ![screenshot](documentation/testing/responsive/detail-mobile-large.png) | ![screenshot](documentation/testing/responsive/bag-mobile-large.png) | ![screenshot](documentation/testing/responsive/checkout-mobile-large.png) | ![screenshot](documentation/testing/responsive/checkout2-mobile-large.png) | ![screenshot](documentation/testing/responsive/edit-mobile-large.png) | ![screenshot](documentation/testing/responsive/add-mobile-large.png) | ![screenshot](documentation/testing/responsive/signin-mobile-large.png) | ![screenshot](documentation/testing/responsive/order-mobile-large.png) | ![screenshot](documentation/testing/responsive/faq-mobile-large.png) |
| Tablet | ![screenshot](documentation/testing/responsive/home-tablet.png) | ![screenshot](documentation/testing/responsive/about-tablet.png) | ![screenshot](documentation/testing/responsive/contact-tablet.png) | ![screenshot](documentation/testing/responsive/records-tablet.png) | ![screenshot](documentation/testing/responsive/detail-teablet.png) | ![screenshot](documentation/testing/responsive/bag-tablet.png) | ![screenshot](documentation/testing/responsive/checkout-tablet.png) | ![screenshot](documentation/testing/responsive/checkout2-tablet.png) | ![screenshot](documentation/testing/responsive/edit-tablet.png) | ![screenshot](documentation/testing/responsive/add-tablet.png) | ![screenshot](documentation/testing/responsive/signin-tablet.png) | ![screenshot](documentation/testing/responsive/order-tablet.png) | ![screenshot](documentation/testing/responsive/faq-tablet.png) |
| Desktop Small | ![screenshot](documentation/testing/responsive/home-desktop-small.png) | ![screenshot](documentation/testing/responsive/about-desktop-small.png) | ![screenshot](documentation/testing/responsive/contact-desktop-small.png) | ![screenshot](documentation/testing/responsive/records-desktop-small.png) | ![screenshot](documentation/testing/responsive/detail-desktop-small.png) | ![screenshot](documentation/testing/responsive/bag-desktop-small.png) | ![screenshot](documentation/testing/responsive/checkout-desktop-small.png) | ![screenshot](documentation/testing/responsive/checkout2-desktop-small.png) | ![screenshot](documentation/testing/responsive/edit-desktop-small.png) | ![screenshot](documentation/testing/responsive/add-desktop-small.png) | ![screenshot](documentation/testing/responsive/signin-desktop-small.png) | ![screenshot](documentation/testing/responsive/order-desktop-small.png) | ![screenshot](documentation/testing/responsive/faq-desktop-small.png) |
| Desktop Medium | ![screenshot](documentation/testing/responsive/home-desktop-medium.png) | ![screenshot](documentation/testing/responsive/about-desktop-medium.png) | ![screenshot](documentation/testing/responsive/contact-desktop-medium.png) | ![screenshot](documentation/testing/responsive/records-desktop-medium.png) | ![screenshot](documentation/testing/responsive/detail-desktop-medium.png) | ![screenshot](documentation/testing/responsive/bag-desktop-medium.png) | ![screenshot](documentation/testing/responsive/checkout-desktop-medium.png) | ![screenshot](documentation/testing/responsive/checkout2-desktop-medium.png) | ![screenshot](documentation/testing/responsive/edit-desktop-medium.png) | ![screenshot](documentation/testing/responsive/add-desktop-medium.png) | ![screenshot](documentation/testing/responsive/signin-desktop-medium.png) | ![screenshot](documentation/testing/responsive/order-desktop-medium.png) | ![screenshot](documentation/testing/responsive/faq-desktop-medium.png) |
| Desktop Large | ![screenshot](documentation/testing/responsive/home-desktop-large.png) | ![screenshot](documentation/testing/responsive/about-desktop-large.png) | ![screenshot](documentation/testing/responsive/contact-desktop-large.png) | ![screenshot](documentation/testing/responsive/records-desktop-large.png) | ![screenshot](documentation/testing/responsive/detail-desktop-large.png) | ![screenshot](documentation/testing/responsive/bag-desktop-large.png) | ![screenshot](documentation/testing/responsive/checkout-desktop-large.png) | ![screenshot](documentation/testing/responsive/checkout2-desktop-large.png) | ![screenshot](documentation/testing/responsive/edit-desktop-large.png) | ![screenshot](documentation/testing/responsive/add-desktop-large.png) | ![screenshot](documentation/testing/responsive/signin-desktop-large.png) | ![screenshot](documentation/testing/responsive/order-desktop-large.png) | ![screenshot](documentation/testing/responsive/faq-dekstop-large.png) |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | some warnings regarding third-party cookies in Best Practice |
| About | ![screenshot](documentation/lighthouse/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-about-desktop.png) | slow on mobile, heroku/amazon. same cookies|
| Records | ![screenshot](documentation/lighthouse/lighthouse-records-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-records-desktop.png) | Slow performance, many images from ams. |
| Details | ![screenshot](documentation/lighthouse/lighthouse-details-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-details-desktop.png) | Slow ams, same cookie warning |
| Bag | ![screenshot](documentation/lighthouse/lighthouse-bag-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-bag-desktop.png) | slow, inc/decr-buttons have no names, links are not crawlable, same cookie warning  |
| Checkout | ![screenshot](documentation/lighthouse/lighthouse-checkout-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-checkout-desktop.png) | Same as others|
| Edit | ![screenshot](documentation/lighthouse/lighthouse-edit-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-edit-desktop.png) | |
| Add | ![screenshot](documentation/lighthouse/lighthouse-add-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-add-desktop.png) | |
| Sign in | ![screenshot](documentation/lighthouse/lighthouse-signin-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-signin-desktop.png) | |


## Defensive Programming

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature01.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature02.png) |
| About | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature03.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature04.png) |
| Gallery | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature05.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature06.png) |
| Contact | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature07.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature08.png) |
| repeat for all remaining pages | x | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Another way of performing defensive testing is a simple Pass/Fail for each test.
The assessors prefer the above method, with the full test explained, but this is also acceptable in most cases.

When in doubt, use the above method instead, and delete the table below.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
|As a new shopper, I would like to view a list of records, so that I can select some and purchase. |![screenshot](documentation/feature_list.png) |
|As a new shopper, I would like to view different genres/categories of Records, so that I can easily find the style I prefer. |![screenshot](documentation/feature_genre.png) |
|As a new shopper, I would like to view a single record, so that I can see its details and make a proper decision. |![screenshot](documentation/feature_singel_record.png) |
|As a new shopper, I would like to be able to register for an account, so that I can see my profile. |![screenshot](documentation/feature_register.png) |
|As a new shopper, I would like to get a confirmation email, so I can verify my account. |![screenshot](documentation/feature_confirmation_email.png) |
|As a new shopper, I want to be able to quickly see if there are any deals to be made. |![screenshot](documentation/feature_deals.png) |
|As a new shopper, I want to be able to quickly see the total amount of my shopping bag to avoid overspending. |![screenshot](documentation/feature_total_amount.png) |
|As a new shopper, I want to be able to search the site for a specific item. |[![Image from Gyazo](https://i.gyazo.com/28af1f02d9d266835e3347fd7c1523bc.gif)](https://gyazo.com/28af1f02d9d266835e3347fd7c1523bc) |
|As a new shopper, I want to be able to view all my items in my shopping bag. |![screenshot](documentation/feature_shopping_bag.png) |
|As a new shopper, I want to be able to sort items to easily find the most rated (if I have created a rating system) or price. |[![Image from Gyazo](https://i.gyazo.com/798eb4a1a1322ee4936fa923a5f99d7f.gif)](https://gyazo.com/798eb4a1a1322ee4936fa923a5f99d7f) |
|As a new shopper, I want to be able to adjust the number of items in my shopping bag. |[![Edit quantity](https://i.gyazo.com/71388a42360733ade872ad7c114b2d5e.gif)](https://gyazo.com/71388a42360733ade872ad7c114b2d5e) |
|As a new shopper, I want to be able to easily enter my payment securely. |![screenshot](documentation/feature_secure_payment.png) |
|As a new shopper, I want to have a confirmation of my order, to easily see that there are no mistakes. |![screenshot](documentation/feature_order_confirmation.png) |
|As a returning Shopper, I would like to easily sign in and out, so that I can access my personal information. |![screenshot](documentation/feature_sign_in_out.png) |
|As a returning Shopper, I would like to have a personal profile, so that I can view my order history, and save my payment information. |![screenshot](documentation/feature_personal_profile.png) |
|As a site administrator, I want to be able to add an item to the store. |![screenshot](documentation/feature_add_item.png) |
|As a site administrator, I want to be able to edit and update items in the store, with prices, images, and various options. |![screenshot](documentation/feature_edit_update.png) |
|As a site administrator, I must be able to remove an item that is no longer available. |![screenshot](documentation/feature_remove_item.png) |

## Bugs


- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.


## Unfixed Bugs
BUGS! 

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.


> [!NOTE]  
> There are no remaining bugs that I am aware of.
