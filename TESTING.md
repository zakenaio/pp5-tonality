# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

In this section, you need to convince the assessors that you have conducted enough testing to legitimately believe that the site works well.
Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended,
with the project providing an easy and straightforward way for the users to achieve their goals.

Feature-by-Feature Testing:

Go through each feature of your portfolio site and detail the testing process for each.

Explain the functionality and demonstrate how it aligns with the intended purpose. This could include:

- Navigation: Ensuring smooth transitions between pages, links directing to the correct destinations.
- Responsive Design: Checking for compatibility across various devices and screen sizes.
- Portfolio Display: Verifying that projects are properly showcased with accurate descriptions, images, and links.
- Contact Form: Testing the form submission process, ensuring the user receives a confirmation, and you receive the message.

User Experience Testing:

- Usability Testing: Have users (or simulated users) interact with the site and provide feedback. Document any issues encountered and the resolutions implemented.
- Accessibility Testing: Confirm compliance with accessibility standards (e.g., screen reader compatibility, proper alt text for images, keyboard navigation).

Compatibility Testing:

- Browser Compatibility: Testing on different browsers (Chrome, Firefox, Safari, Edge, etc.) to ensure consistent performance.
- Device Compatibility: Ensuring functionality across various devices (desktops, laptops, tablets, and mobile phones).
- Performance Testing (optional):
	- Speed and Load Testing: Tools like PageSpeed Insights or GTmetrix to check page load times and optimize where necessary.
	- Scalability Testing: Assess how the site handles increased traffic or usage.

Regression Testing:

After implementing fixes or updates, ensure that previous features and functionalities still work as intended. This prevents new changes from breaking existing features.

Documentation and Logs:

Maintain records of testing procedures, results, and any bugs encountered along with their resolutions. This helps demonstrate a systematic approach to testing and problem-solving.
User Feedback Incorporation:

If applicable, mention how user feedback has been taken into account and implemented to enhance the user experience.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

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
| records | custom_clearable_file_input.html | ![screenshot](documentation/testing/html-custom_clearable_file_input.png) | |
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
| Tablet | ![screenshot](documentation/testing/responsive/home-tablet.png) | ![screenshot](documentation/testing/responsive/about-tablet.png) | ![screenshot](documentation/testing/responsive/contact-tablet.png) | ![screenshot](documentation/testing/responsive/records-tablet.png) | ![screenshot](documentation/testing/responsive/detail-tablet.png) | ![screenshot](documentation/testing/responsive/bag-tablet.png) | ![screenshot](documentation/testing/responsive/checkout-tablet.png) | ![screenshot](documentation/testing/responsive/checkout2-tablet.png) | ![screenshot](documentation/testing/responsive/edit-tablet.png) | ![screenshot](documentation/testing/responsive/add-tablet.png) | ![screenshot](documentation/testing/responsive/signin-tablet.png) |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings |
| About | ![screenshot](documentation/lighthouse/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-about-desktop.png) | Some minor warnings |
| Gallery | ![screenshot](documentation/lighthouse/lighthouse-gallery-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| x | x | x | repeat for any other tested pages/sizes |

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

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## User Story Testing

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature09.png) |
| repeat for all remaining user stories | x |

## Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

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

### GitHub **Issues**

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/zakenaio/pp5-tonality/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Azakenaio%2Fpp5-tonality%20label%3Abug&label=bugs)](https://github.com/zakenaio/pp5-tonality/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/zakenaio/pp5-tonality/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/zakenaio/pp5-tonality/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/zakenaio/pp5-tonality/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/zakenaio/pp5-tonality/issues/3) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/zakenaio/pp5-tonality)](https://github.com/zakenaio/pp5-tonality/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/zakenaio/pp5-tonality)](https://github.com/zakenaio/pp5-tonality/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/zakenaio/pp5-tonality/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/zakenaio/pp5-tonality/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/zakenaio/pp5-tonality/issues/5) | Open |

## Unfixed Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.
