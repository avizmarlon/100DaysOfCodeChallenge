Most tags can easily be remembered by their "full name", e.g.:
<ul> = unordered list, the tag is made by the initials of the full name, same as <ol> = ordered list or <li> = list item
<p> = paragraph
<h1...h6> = header1...header6

This makes it pretty easy to remember them. The tags are usually self-descriptive when you think about it.

--------------

Remembering the best practice of setting a for attribute in a label element nesting an input element with an id attribute to aid assistive tech in creating relationships between those elements.

This <label> is "for" the nested <input> "id"entified by id="id".

<label for="awesome-input>
    <input id="awesome-input">
</label>

Extra tip: this also allows the user to click any part of the text associated with a button to select an option instead of having to click the button itself. Small, but quality-of-life adjustments like this goes a long way for the user experience.

Example:

<form>
<label for="blue-input">
    <input type="radio" id="blue-input" name="blue-red"> Blue
</label>

<label for="red-input">
    <input type="radio" id="red-input" name="blue-red"> Red
</label>
</form>

This creates a form with two radio buttons (only 1 option can be selected by the user) grouped by the name "blue-red". Each with a text next to them (first option with "Blue" and second option with "Red"). The <label> allows the user, for instance, to click the text "Blue" to select the radio button, instead of having to click the radio button itself.

--------------

Input elements of the type "radio" and "checkboxes" submit (when user press the "submit" button, for example) their data from their "value" attribute, not the "name" or "id" attributes, and not the text value of the input element.

The resulting form data is written in the format: name_attribute=value_attribute

Example:

<label for="number1">
    <input type="radio" id="number1" name="numbers" value="number1"> Number 1
</label>
<label for="number2">
    <input type="checkbox" id="number2" name="numbers" value="number2"> Number 2
</label>

If the user selects the first option (Number 1), the submitted form data would be numbers=number1

"numbers" is the value of the "name" attribute by which both buttons are associated by.
"number1" is the value of the "Value" attribute of the chosen option (Number 1).

If the chosen option doesn't have a "Value" attribute or it's empty, it will default to "on", which isn't meaningful; its as bad as naming a variable "Variable", and is bound to cause confusion in the future.

--------------