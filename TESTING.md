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
| about | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/about/urls.py) | ![Pep about urls](documentation/testing/validation/pep8-about-urls.png) | |
| about | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/about/views.py) | ![Pep8 about views](documentation/testing/validation/pep8-about-views.png) | |
| Directory | File | CI URL | Screenshot | Notes |
| bag | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/bag/contexts.py) | ![Pep8 bag context](documentation/testing/validation/pep8-bag-contexts.png) | |
| bag | bag_tools.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/bag/templatetags/bag_tools.py) | ![Pep8 bag bagtools](documentation/testing/validation/pep8-bag-bagtools.png) | |
| bag | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/bag/urls.py) | ![Pep 8 bag urls](documentation/testing/validation/pep8-bag-url.png) |  |
| bag | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/bag/views.py) | ![Pep8 bag views](documentation/testing/validation/pep8-bag-views.png) | A  long line. |
| checkout | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/admin.py) | ![Pep8 checkout admin](documentation/testing/validation/pep8-checkout-admin.png) | |
| checkout | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/forms.py) | ![Pep8 checkout forms](documentation/testing/validation/pep8-checkout-forms.png) | |
| checkout | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/models.py) | ![Pep8 checkout models](documentation/testing/validation/pep8-checkout-models.png) | A long line. |
| checkout | signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/signals.py) | ![Pep8 checkout signals](documentation/testing/validation/pep8-checkout-signals.png) | |
| checkout | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/urls.py) | ![Pep8 checkout urls](documentation/testing/validation/pep8-checkout-urls.png) | Two long lines |
| checkout | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/views.py) | ![Pep8 checkout views](documentation/testing/validation/pep8-checkout-views.png) | Two long lines |
| checkout | webhook_handler.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/webhook_handler.py) | ![Pep8 checkout whh](documentation/testing/validation/pep8-checkout-whh.png) | Several long lines |
| checkout | webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/checkout/webhooks.py) | ![Pep8 checkout wh](documentation/testing/validation/pep8-checkout-wh.png) | Two long lines |
| contact | context_processors.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/contact/context_processors.py) | ![Pep8 contact contentproc](documentation/testing/validation/pep8-contact-context.png) | |
| contact | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/contact/forms.py) | ![Pep8 contact forms](documentation/testing/validation/pep8-contact-forms.png) | |
| contact | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/contact/models.py) | ![Pep8 contact models](documentation/testing/validation/pep8-contact-models.png) | |
| contact | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/contact/urls.py) | ![Pep8 contact urls](documentation/testing/validation/pep8-contact-urls.png) | |
| contact | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/contact/views.py) | ![Pep8 contact views](documentation/testing/validation/pep8-contact-views.png) | |
| faq | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/faq/admin.py) | ![Pep8 faq admin](documentation/testing/validation/pep8-faq-admin.png) | |
| faq | context_processors.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/faq/context_processors.py) | ![Pep8 faq contextproc](documentation/testing/validation/pep8-faq-context.png) | |
| faq | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/faq/models.py) | ![Pep8 faq models](documentation/testing/validation/pep8-faq-models.png) | |
| faq | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/faq/urls.py) | ![Pep8 faq urls](documentation/testing/validation/pep8-faq-urls.png) | |
| faq | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/faq/views.py) | ![Pep8 faq views](documentation/testing/validation/pep8-faq-views.png) | |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/home/urls.py) | ![Pep8 home urls](documentation/testing/validation/pep8-home-urls.png) | |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/home/views.py) | ![Pep8 home views](documentation/testing/validation/pep8-home-views.png) | |
| newsletter | content_processor.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/newsletter/content_processor.py) | ![Pep8 newsletter context](documentation/testing/validation/pep8-newsletter-context.png) | |
| newsletter | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/newsletter/forms.py) | ![Pep8 newsletter forns](documentation/testing/validation/pep8-newsletter-forms.png) | |
| newsletter | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/newsletter/models.py) | ![Pep8 newsletter models](documentation/testing/validation/pep8-newsletter-models.png) | |
| newsletter | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/newsletter/urls.py) | ![Pep8 newsletter urls](documentation/testing/validation/pep8-newsletter-urls.png) | |
| newsletter | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/newsletter/views.py) | ![Pep8 newsletter views](documentation/testing/validation/pep8-newsletter-views.png) | Few longer lines |
| profiles | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/profiles/forms.py) | ![Pep8 profiles forms](documentation/testing/validation/pep8-profiles-forms.png) | A longer line |
| profiles | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/profiles/models.py) | ![Pep8 profiles models](documentation/testing/validation/pep8-profiles-models.png) | |
| profiles | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/profiles/urls.py) | ![Pep8 profiles urls](documentation/testing/validation/pep8-profiles-urls.png) | |
| profiles | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/profiles/views.py) | ![Pep8 profiles views](documentation/testing/validation/pep8-profiles-views.png) | |
| records | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/records/admin.py) | ![Pep8 records admin](documentation/testing/validation/pep8-records-admin.png) | A longer line |
| records | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/records/forms.py) | ![Pep8 records forms](documentation/testing/validation/pep8-records-forms.png) | |
| records | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/records/models.py) | ![Pep8 records models](documentation/testing/validation/pep8-records-models.png) | |
| records | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/records/urls.py) | ![Pep8 records urls](documentation/testing/validation/pep8-records-urls.png) | |
| records | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/records/views.py) | ![Pep8 records views](documentation/testing/validation/pep8-records-views.png) | A longer line |
| records | widgets.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/records/widgets.py) | ![Pep8 records widgets](documentation/testing/validation/pep8-records-widgets.png) | A longer line |
| tonality | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/tonality/urls.py) | ![Pep8 urls](documentation/testing/validation/pep8-tonality-urls.png) | |
|  | custom_storages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/zakenaio/pp5-tonality/main/custom_storages.py) | ![Pep8 custom storage](documentation/testing/validation/pep8-customstorage.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | Records | Details | Bag | Checkout  | Edit | Add | Sign in | Faq |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Brave Win 11 | ![screenshot](documentation/testing/responsive/home-brave-win11.png) | ![screenshot](documentation/testing/responsive/about-brave-win11.png) | ![screenshot](documentation/testing/responsive/contact-brave-win11.png) | ![screenshot](documentation/testing/responsive/records-brave-win11.png) | ![screenshot](documentation/testing/responsive/detail-brave-win11.png) | ![screenshot](documentation/testing/responsive/bag-brave-win11.png) | ![screenshot](documentation/testing/responsive/checkout-brave-win11.png) | ![screenshot](documentation/testing/responsive/edit-brave-win11.png) | ![screenshot](documentation/testing/responsive/add-brave-win11.png) | ![screenshot](documentation/testing/responsive/signin-brave-win11.png) | ![screenshot](documentation/testing/responsive/faq-brave-win11.png) |
| Edge Win 11 | ![screenshot](documentation/testing/responsive/home-edge-win11.png) | ![screenshot](documentation/testing/responsive/about-edge-win11.png) | ![screenshot](documentation/testing/responsive/contact-edge-win11.png) | ![screenshot](documentation/testing/responsive/records-edge-win11.png) | ![screenshot](documentation/testing/responsive/detail-edge-win11.png) | ![screenshot](documentation/testing/responsive/bag-edge-win11.png) | ![screenshot](documentation/testing/responsive/checkout-edge-win11.png) | ![screenshot](documentation/testing/responsive/edit-edge-win11.png) | ![screenshot](documentation/testing/responsive/add-edge-win11.png) | ![screenshot](documentation/testing/responsive/signin-edge-win11.png) | ![screenshot](documentation/testing/responsive/faq-edge-win11.png) |
| Safari Mac | ![screenshot](documentation/testing/responsive/home-safari-mac.png) | ![screenshot](documentation/testing/responsive/about-safari-mac.png) | ![screenshot](documentation/testing/responsive/contact-safari-mac.png) | ![screenshot](documentation/testing/responsive/records-safari-mac.png) | ![screenshot](documentation/testing/responsive/detail-safari-mac.png) | ![screenshot](documentation/testing/responsive/bag-safari-mac.png) | ![screenshot](documentation/testing/responsive/checkout-safari-mac.png) | ![screenshot](documentation/testing/responsive/edit-safari-mac.png) | ![screenshot](documentation/testing/responsive/add-safari-mac.png) | ![screenshot](documentation/testing/responsive/signin-safari-mac.png) | ![screenshot](documentation/testing/responsive/faq-safari-mac.png) |
| Firefox Mac | ![screenshot](documentation/testing/responsive/home-firefox-mac.png) | ![screenshot](documentation/testing/responsive/about-firefox-mac.png) | ![screenshot](documentation/testing/responsive/contact-firefox-mac.png) | ![screenshot](documentation/testing/responsive/records-firefox-mac.png) | ![screenshot](documentation/testing/responsive/detail-firefox-mac.png) | ![screenshot](documentation/testing/responsive/bag-firefox-mac.png) | ![screenshot](documentation/testing/responsive/checkout-firefox-mac.png) | ![screenshot](documentation/testing/responsive/edit-firefox-mac.png) | ![screenshot](documentation/testing/responsive/add-firefox-mac.png) | ![screenshot](documentation/testing/responsive/signin-firefox-mac.png) | ![screenshot](documentation/testing/responsive/faq-firefox-mac.png) |
| Firefox Linux | ![screenshot](documentation/testing/responsive/home-firefox-linux.png) | ![screenshot](documentation/testing/responsive/about-firefox-linux.png) | ![screenshot](documentation/testing/responsive/contact-firefox-linux.png) | ![screenshot](documentation/testing/responsive/records-firefox-linux.png) | ![screenshot](documentation/testing/responsive/detail-firefox-linux.png) | ![screenshot](documentation/testing/responsive/bag-firefox-linux.png) | ![screenshot](documentation/testing/responsive/checkout-firefox-linux.png) | ![screenshot](documentation/testing/responsive/edit-firefox-linux.png) | ![screenshot](documentation/testing/responsive/add-firefox-linux.png) | ![screenshot](documentation/testing/responsive/signin-firefox-linux.png) | ![screenshot](documentation/testing/responsive/faq-firefox-linux.png) |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | Records | Details | Bag | Checkout | Checkout2 | Edit | Add | Sign in | Order | Faq |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile Small | ![Home Mobile Small](documentation/testing/responsive/home-mobile-small.png) | ![About Mobile Small](documentation/testing/responsive/about-mobile-small.png) | ![Contact Mobile Small](documentation/testing/responsive/contact-mobile-small.png) | ![Records Mobile Small](documentation/testing/responsive/records-mobile-small.png) | ![Detail Mobile Small](documentation/testing/responsive/detail-mobile-small.png) | ![Bag Mobile Small](documentation/testing/responsive/bag-mobile-small.png) | ![Checkout Mobile Small](documentation/testing/responsive/checkout-mobile-small.png) | ![Checkout2 Mobile Small](documentation/testing/responsive/checkout2-mobile-small.png) | ![Edit Mobile Small](documentation/testing/responsive/edit-mobile-small.png) | ![Add Mobile Small](documentation/testing/responsive/add-mobile-small.png) | ![Signin Mobile Small](documentation/testing/responsive/signin-mobile-small.png) | ![Order Mobile Small](documentation/testing/responsive/order-mobile-small.png) | ![Faq Mobile Small](documentation/testing/responsive/faq-mobile-small.png) |
| Mobile Medium | ![Home Mobile Medium](documentation/testing/responsive/home-mobile-medium.png) | ![About Mobile Medium](documentation/testing/responsive/about-mobile-medium.png) | ![Contact Mobile Medium](documentation/testing/responsive/contact-mobile-medium.png) | ![Records Mobile Medium](documentation/testing/responsive/records-mobile-medium.png) | ![Detail Mobile Medium](documentation/testing/responsive/detail-mobile-medium.png) | ![Bag Mobile Medium](documentation/testing/responsive/bag-mobile-medium.png) | ![Checkout Mobile Medium](documentation/testing/responsive/checkout-mobile-medium.png) | ![Checkout2 Mobile Medium](documentation/testing/responsive/checkout2-mobile-medium.png) | ![Edit Mobile Medium](documentation/testing/responsive/edit-mobile-medium.png) | ![Add Mobile Medium](documentation/testing/responsive/add-mobile-medium.png) | ![Signin Mobile Medium](documentation/testing/responsive/signin-mobile-medium.png) | ![Order Mobile Medium](documentation/testing/responsive/order-mobile-medium.png) | ![Faq Mobile Medium](documentation/testing/responsive/faq-mobile-medium.png) |
| Mobile Large | ![Home Mobile Large](documentation/testing/responsive/home-mobile-large.png) | ![About Mobile Large](documentation/testing/responsive/about-mobile-large.png) | ![Contact Mobile Large](documentation/testing/responsive/contact-mobile-large.png) | ![Records Mobile Large](documentation/testing/responsive/records-mobile-large.png) | ![Detail Mobile Large](documentation/testing/responsive/detail-mobile-large.png) | ![Bag Mobile Large](documentation/testing/responsive/bag-mobile-large.png) | ![Checkout Mobile Large](documentation/testing/responsive/checkout-mobile-large.png) | ![Checkout2 Mobile Large](documentation/testing/responsive/checkout2-mobile-large.png) | ![Edit Mobile Large](documentation/testing/responsive/edit-mobile-large.png) | ![Add Mobile Large](documentation/testing/responsive/add-mobile-large.png) | ![Signin Mobile Large](documentation/testing/responsive/signin-mobile-large.png) | ![Order Mobile Large](documentation/testing/responsive/order-mobile-large.png) | ![Faq Mobile Large](documentation/testing/responsive/faq-mobile-large.png) |
| Tablet | ![Home Tablet](documentation/testing/responsive/home-tablet.png) | ![About Tablet](documentation/testing/responsive/about-tablet.png) | ![Contact Tablet](documentation/testing/responsive/contact-tablet.png) | ![Records Tablet](documentation/testing/responsive/records-tablet.png) | ![Detail Tablet](documentation/testing/responsive/detail-teablet.png) | ![Bag Tablet](documentation/testing/responsive/bag-tablet.png) | ![Checkout Tablet](documentation/testing/responsive/checkout-tablet.png) | ![Checkout2 Tablet](documentation/testing/responsive/checkout2-tablet.png) | ![Edit Tablet](documentation/testing/responsive/edit-tablet.png) | ![Add Tablet](documentation/testing/responsive/add-tablet.png) | ![Signin Tablet](documentation/testing/responsive/signin-tablet.png) | ![Order Tablet](documentation/testing/responsive/order-tablet.png) | ![Faq Tablet](documentation/testing/responsive/faq-tablet.png) |
| Desktop Small | ![Home Desktop Small](documentation/testing/responsive/home-desktop-small.png) | ![About Desktop Small](documentation/testing/responsive/about-desktop-small.png) | ![Contact Desktop Small](documentation/testing/responsive/contact-desktop-small.png) | ![Records Desktop Small](documentation/testing/responsive/records-desktop-small.png) | ![Detail Desktop Small](documentation/testing/responsive/detail-desktop-small.png) | ![Bag Desktop Small](documentation/testing/responsive/bag-desktop-small.png) | ![Checkout Desktop Small](documentation/testing/responsive/checkout-desktop-small.png) | ![Checkout2 Desktop Small](documentation/testing/responsive/checkout2-desktop-small.png) | ![Edit Desktop Small](documentation/testing/responsive/edit-desktop-small.png) | ![Add Desktop Small](documentation/testing/responsive/add-desktop-small.png) | ![Signin Desktop Small](documentation/testing/responsive/signin-desktop-small.png) | ![Order Desktop Small](documentation/testing/responsive/order-desktop-small.png) | ![Faq Desktop Small](documentation/testing/responsive/faq-desktop-small.png) |
| Desktop Medium | ![Home Desktop Medium](documentation/testing/responsive/home-desktop-medium.png) | ![About Desktop Medium](documentation/testing/responsive/about-desktop-medium.png) | ![Contact Desktop Medium](documentation/testing/responsive/contact-desktop-medium.png) | ![Records Desktop Medium](documentation/testing/responsive/records-desktop-medium.png) | ![Detail Desktop Medium](documentation/testing/responsive/detail-desktop-medium.png) | ![Bag Desktop Medium](documentation/testing/responsive/bag-desktop-medium.png) | ![Checkout Desktop Medium](documentation/testing/responsive/checkout-desktop-medium.png) | ![Checkout2 Desktop Medium](documentation/testing/responsive/checkout2-desktop-medium.png) | ![Edit Desktop Medium](documentation/testing/responsive/edit-desktop-medium.png) | ![Add Desktop Medium](documentation/testing/responsive/add-desktop-medium.png) | ![Signin Desktop Medium](documentation/testing/responsive/signin-desktop-medium.png) | ![Order Desktop Medium](documentation/testing/responsive/order-desktop-medium.png) | ![Faq Desktop Medium](documentation/testing/responsive/faq-desktop-medium.png) |
| Desktop Large | ![Home Desktop Large](documentation/testing/responsive/home-desktop-large.png) | ![About Desktop Large](documentation/testing/responsive/about-desktop-large.png) | ![Contact Desktop Large](documentation/testing/responsive/contact-desktop-large.png) | ![Records Desktop Large](documentation/testing/responsive/records-desktop-large.png) | ![Detail Desktop Large](documentation/testing/responsive/detail-desktop-large.png) | ![Bag Desktop Large](documentation/testing/responsive/bag-desktop-large.png) | ![Checkout Desktop Large](documentation/testing/responsive/checkout-desktop-large.png) | ![Checkout2 Desktop Large](documentation/testing/responsive/checkout2-desktop-large.png) | ![Edit Desktop Large](documentation/testing/responsive/edit-desktop-large.png) | ![Add Desktop Large](documentation/testing/responsive/add-desktop-large.png) | ![Signin Desktop Large](documentation/testing/responsive/signin-desktop-large.png) | ![Order Desktop Large](documentation/testing/responsive/order-desktop-large.png) | ![Faq Desktop Large](documentation/testing/responsive/faq-dekstop-large.png) |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![Lighthouse home mobile](documentation/lighthouse/lighthouse-home-mobile.png) | ![Lighthouse home desktop](documentation/lighthouse/lighthouse-home-desktop.png) | some warnings regarding third-party cookies in Best Practice |
| About | ![Lighthouse about mobile](documentation/lighthouse/lighthouse-about-mobile.png) | ![Lighthouse about desktop](documentation/lighthouse/lighthouse-about-desktop.png) | slow on mobile, heroku/amazon. same cookies|
| Records | ![Lighthouse records mobile](documentation/lighthouse/lighthouse-records-mobile.png) | ![Lighthouse records desktop](documentation/lighthouse/lighthouse-records-desktop.png) | Slow performance, many images from ams. |
| Details | ![Lighthouse details mobile](documentation/lighthouse/lighthouse-details-mobile.png) | ![Lighthouse details desktop](documentation/lighthouse/lighthouse-details-desktop.png) | Slow ams, same cookie warning |
| Bag | ![Lighthouse bag mobile](documentation/lighthouse/lighthouse-bag-mobile.png) | ![Lighthouse bag desktop](documentation/lighthouse/lighthouse-bag-desktop.png) | slow, inc/decr-buttons have no names, links are not crawlable, same cookie warning  |
| Checkout | ![Lighthouse checkout mobile](documentation/lighthouse/lighthouse-checkout-mobile.png) | ![Lighthouse checkout desktop](documentation/lighthouse/lighthouse-checkout-desktop.png) | Same as others|
| Edit | ![Lighthouse edit mobile](documentation/lighthouse/lighthouse-edit-mobile.png) | ![Lighthouse edit desktop](documentation/lighthouse/lighthouse-edit-desktop.png) | |
| Add | ![Lighthouse add mobile](documentation/lighthouse/lighthouse-add-mobile.png) | ![Lighthouse add desktop](documentation/lighthouse/lighthouse-add-desktop.png) | |
| Sign in | ![Lighthouse sign in mobile](documentation/lighthouse/lighthouse-signin-mobile.png) | ![Lighthouse sign in desktop](documentation/lighthouse/lighthouse-signin-desktop.png) | |


## Defensive Programming

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Clicking on a menu item brings me to the page | Does menu appear when clicked? | When clicked a menu appears, and you are redirected to the clicked page | Test concluded and passed | [![Menu](https://i.gyazo.com/ad9db4341ffe6745a0f80d54ef6829d7.gif)](https://gyazo.com/ad9db4341ffe6745a0f80d54ef6829d7) |
| | Entering a search term and clicking the magnifying glass should give me search results | tested by typing a seach quiery | page refresh an a result was shown |  | [![Search](https://i.gyazo.com/fef0c1a4542c313f13c398e1eea86053.gif)](https://gyazo.com/fef0c1a4542c313f13c398e1eea86053) |
| Records | | | | | |
| | When hovering over a Record cover, the button for adding to bag should appear. | Hover over a record cover to see if the add to bag button appears. | The button appeared as expected. | Test concluded and passed | [![Add to bag](https://i.gyazo.com/39032d9e96e651404670e1d88635cc66.gif)](https://gyazo.com/39032d9e96e651404670e1d88635cc66) |
| | Filtering records by genre should display only records from the selected genre. | Select a genre from the filter options and observe the records displayed. | Only records from the selected genre were displayed. | Test concluded and passed | [![Filter by Genere](https://i.gyazo.com/e2bb7bae06db972834cf191b8ac0c125.gif)](https://gyazo.com/e2bb7bae06db972834cf191b8ac0c125) |
| | Sorting records by price, from low to high, should reorder the records accordingly. | Select the "Price Low to High" sorting option and observe the order of records. | Records were reordered from lowest to highest price as expected. | Test concluded and passed | [![Sort](https://i.gyazo.com/047c10abb69d54dda62d512dd8d0803b.gif)](https://gyazo.com/047c10abb69d54dda62d512dd8d0803b) |
| | Searching for a record by name should display relevant results. | Type a record name in the search bar and submit the search. | The search returned records with matching names. | Test concluded and passed | [![Search Record](https://i.gyazo.com/cf1bf0c2a5253f004a375a55becd7038.gif)](https://gyazo.com/cf1bf0c2a5253f004a375a55becd7038) |
| | Viewing record details should display all relevant information about the record. | Click on a record to view its details. | The details page displayed all relevant information including tracklist, genre, and price. | Test concluded and passed | [![Record Details](https://i.gyazo.com/0adcdf291d6b435e36c663d5f351d1ef.gif)](https://gyazo.com/0adcdf291d6b435e36c663d5f351d1ef) |
| Bag | | | | | |
| | Clicking on the "View Bag" button should take me to the bag page | Click "View Bag" after adding items | Redirects to the bag page with items listed | Test concluded and passed | [![View Bag](https://i.gyazo.com/8df8a17706039980f55d01b3abf5984f.gif)](https://gyazo.com/8df8a17706039980f55d01b3abf5984f) |
| | Updating the quantity of an item in the bag should reflect the correct total price | Change quantity and click "Update" | Total price updates accordingly | Test concluded and passed | [![Update Quantity](https://i.gyazo.com/9249065dadf2bf6e1274bc4e208ad4e7.gif)](https://gyazo.com/9249065dadf2bf6e1274bc4e208ad4e7) |
| | Removing an item from the bag should remove it from the list and update the total price | Click "Remove" on an item | Item is removed and total price updates | Test concluded and passed | [![Remove Item](https://i.gyazo.com/c4f3bb3c790f158d4c9be7f574ce88b2.gif)](https://gyazo.com/c4f3bb3c790f158d4c9be7f574ce88b2) |
| | Order verification on Order | There should be a verification of the order on screen | | Test concluded and passed | ![Order verification](documentation/testing/order-verification.png) |
| Edit | | | | | |
| | Editing a record's details should update the record with the new information | Modify details and save | Record is updated with new details | Test concluded and passed | [![Edit Record](https://i.gyazo.com/2b902c73629acd6108191b34ed5b18d1.gif)](https://gyazo.com/2b902c73629acd6108191b34ed5b18d1) |
| | Trying to reach any edit functinality, even trhough URL you need to be signed in  | User should be redirected to login | Tried entering edit URL | Test concluded and passed | ![CRUD Redirect](documentation/testing/reach-edit-signin.png) |
| Add | | | | | |
| | Adding a new record should list it in the records page | Fill in details and save | New record appears in the list | Test concluded and passed | [![Add Record](https://i.gyazo.com/27fb0844a87fd705ad89b245ff7f10a4.gif)](https://gyazo.com/27fb0844a87fd705ad89b245ff7f10a4) |
| | Required fields must be filled to successfully add a record | Attempt to save with missing required fields | Error messages for missing fields displayed | Test concluded and passed | [![Required Fields](https://i.gyazo.com/f713134681b63c60c567ef6a6bb61eee.gif)](https://gyazo.com/f713134681b63c60c567ef6a6bb61eee) |
| Sign In | | | | | |
| | Entering correct credentials should sign the user in | Enter username and password and submit | User is signed in and redirected to the homepage | Test concluded and passed | [![Sign In](https://i.gyazo.com/a0afda4052d2531ed7c4ae085a04305c.gif)](https://gyazo.com/a0afda4052d2531ed7c4ae085a04305c) |
| | Entering incorrect credentials should display an error message | Enter incorrect username or password and submit | Error message displayed, preventing sign in | Test concluded and passed | [![Sign In Error](https://i.gyazo.com/fdfee5bae6194e165d1a1a7bb9e64007.gif)](https://gyazo.com/fdfee5bae6194e165d1a1a7bb9e64007) |
| | Signing out should redirect the user to the homepage | Click the sign-out button | User is signed out and redirected to the homepage | Test concluded and passed | [![Sign Out](https://i.gyazo.com/99909d56eb23ad288f1b7105d1eba133.gif)](https://gyazo.com/99909d56eb23ad288f1b7105d1eba133) |
| Sign Up | | | | | |
| | Filling in the registration form correctly should create a new user account | Fill in the registration form and submit | New user account is created and confirmation email is sent | Test concluded and passed | [![Sign up Verification](https://i.gyazo.com/a77b34f54e079a76e9e1c7e6c87ada3a.gif)](https://gyazo.com/a77b34f54e079a76e9e1c7e6c87ada3a) |
| | Attempting to register with an already used email should display an error | Use an email already in the system and submit | Error message displayed, preventing account creation | Test concluded and passed | [![Sign up error](https://i.gyazo.com/91fe643dc85af73bed546971f8cceb2d.gif)](https://gyazo.com/91fe643dc85af73bed546971f8cceb2d) |
| Contact | | | | | |
| | Filling out the contact form i want a confirmation of the sent message | Fill in the contact form and submit | Visual feedback is given | Test concluded and passed | [![Contact](https://i.gyazo.com/6aa9310b074f7791b895665275ed539e.gif)](https://gyazo.com/6aa9310b074f7791b895665275ed539e) |
| Newsletter | | | | | |
| | Subscribing to the newsletter should confirm my subscription | Enter email and click subscribe | Confirmation message displayed | Test concluded and passed | [![subscribe](https://i.gyazo.com/00277502abb36b51b2aa4e5e30abb0a1.gif)](https://gyazo.com/00277502abb36b51b2aa4e5e30abb0a1) |
| | Attempting to subscribe with an already subscribed email should display an error message | Use an email already subscribed and submit | Error message displayed, indicating already subscribed | Test concluded and passed | ![Subscribe error](documentation/testing/newsletter-error.png) |
| | A letter should be sent | Look at the console | Message is displayed | Test concluded and passed | ![Newsletter Console](documentation/testing/newletter-console.png) |
| | Letter in mailbox | There should be a letter in my mailbox | | Test concluded and passed | ![Newsletter Console](documentation/testing/newsletter-.welcome.png) |


## User Story Testing

| User Story | Screenshot |
| --- | --- |
|As a new shopper, I would like to view a list of records, so that I can select some and purchase. |![List of Records](documentation/feature_list.png) |
|As a new shopper, I would like to view different genres/categories of Records, so that I can easily find the style I prefer. |![Genres/Categories](documentation/feature_genre.png) |
|As a new shopper, I would like to view a single record, so that I can see its details and make a proper decision. |![Single Record Details](documentation/feature_singel_record.png) |
|As a new shopper, I would like to be able to register for an account, so that I can see my profile. |![Register Account](documentation/feature_register.png) |
|As a new shopper, I would like to get a confirmation email, so I can verify my account. |![Confirmation Email](documentation/feature_order_confirmation.png) |
|As a new shopper, I want to be able to quickly see if there are any deals to be made. |![Deals](documentation/feature_deals.png) |
|As a new shopper, I want to be able to quickly see the total amount of my shopping bag to avoid overspending. |![Total Amount](documentation/feature_total_amount.png) |
|As a new shopper, I want to be able to search the site for a specific item. |[![Search Functionality](https://i.gyazo.com/28af1f02d9d266835e3347fd7c1523bc.gif)](https://gyazo.com/28af1f02d9d266835e3347fd7c1523bc) |
|As a new shopper, I want to be able to view all my items in my shopping bag. | ![Shopping Bag Items](documentation/feature_shopping_bag.png) |
|As a new shopper, I want to be able to sort on price, and rating. |[![Sort by Price and Rating](https://i.gyazo.com/047c10abb69d54dda62d512dd8d0803b.gif)](https://gyazo.com/047c10abb69d54dda62d512dd8d0803b) |
|As a new shopper, I would like to view different genres/categories of Records, so that I can easily find the style I prefer. |![Genres/Categories](documentation/feature_genre.png) |
|As a new shopper, I want to be able to adjust the number of items in my shopping bag. |[![Adjust Quantity](https://i.gyazo.com/71388a42360733ade872ad7c114b2d5e.gif)](https://gyazo.com/71388a42360733ade872ad7c114b2d5e) |
|As a new shopper, I want to be able to easily enter my payment securely. |![Secure Payment](documentation/feature_secure_payment.png) |
|As a new shopper, I want to have a confirmation of my order, to easily see that there are no mistakes. |![Order Confirmation](documentation/feature_order_confirmation.png) |
|As a returning Shopper, I would like to easily sign in and out, so that I can access my personal information. |![Sign In/Out](documentation/feature_sign_in_out.png) |
|As a returning Shopper, I would like to have a personal profile, so that I can view my order history, and save my payment information. |![Personal Profile](documentation/feature_personal_profile.png) |
|As a site administrator, I want to be able to add an item to the store. |![Add Item](documentation/feature_add_item.png) |
|As a site administrator, I want to be able to edit and update items in the store, with prices, images, and various options. |![Edit/Update Items](documentation/feature_edit_update.png) |
|As a site administrator, I must be able to remove an item that is no longer available. |![Remove Item](documentation/feature_remove_item.png) |

## Bugs


- Experienced a small issue with seach term.

    ![screenshot](documentation/testing/bug-search.png)

    - Issue with a line break in the lin {{ seach.term }} making it not render correctly.



> [!NOTE]  
> There are no remaining bugs that I am aware of.
