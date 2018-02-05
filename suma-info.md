All interesting files are in `src/components` and `src/utils`. They correspond to the SUSE Manager files in `web/html/src/`.

## Things I changed:
- Removed `"use strict";` from all components as that should only be neccessary in the top-level js file, also my compiler complains about it
- `utils/network.js` is unchanged (but you should change `==` to `===`)
- `utils/functions.js`: Moved the `generatePassword()` function here. Also some other small fixes:
    - Removed unneccessary `require('react')`
    - Removed unneccessary escapes in regex: `\.\*` -> `.*`
    - Added base to `parseInt()`: `parseInt(..., 10)`
- `components/buttons.js` is unchanged (but you should also change `==` and remove the useless constructors)
- `components/messages.js`: Fixed deprecated `React.createClass()` stuff. Not neccessary but better like this.
- `components/FormulaForm.js`:
    - Cleaned up and moved component rendering to the `components/formulas` directory
    - Renamed the `currentScope` prop to `scope`
    - Replaced the `saveFormula` function prop by a `saveUrl` and `systemId` prop. `systemId` is the id of the server or group the formula page belongs to.
    - Removed the "Feature preview" message. You probably want to keep it, see notes below.
    - Added `const $ = require("jquery");`. You probably don't need this.
- `components/formula-selection.js`:
    - Replaced the `toTitle()` function by the `capitalize` function from `utils/functions.js`
- Formula components are now rendered by a function in `components/forumlas/FormulaComponentGenerator.js` and more complicated components have their own file in the same directory
- All the formula css is in `components/FormulaForm.css`. Most of that is already in the SUSE Manager stylesheet, but the `edit-group` stuff at the bottom needs to go into the stylesheet.

## Basically:
1. You can copy the js files from `src/utils` and `src/components` over if their weren't any new changes to the files. You can leave `utils/network.js`, `components/buttons.js`, `components/messages.js` and `components/formula-selection.js` out if you want/need to.
2. Copy all the `edit-group` style-rules from `components/FormulaForm.css` into the SUSE Manager stylesheet.
3. Remove the `const $ = require("jquery");` line at the top of `components/FormulaForm.js`
4. Add the "Feature preview" message back in:
    1. In the constructor of `components/FormulaForm.js` add this line before the initial state assignement:

        `const previewMessage = <p><strong>{t('This is a feature preview')}</strong>: On this page you can configure <a href="https://docs.saltstack.com/en/latest/topics/development/conventions/formulas.html" target="_blank" rel="noopener noreferrer">Salt formulas</a> to automatically install and configure software. We would be glad to receive your feedback via the <a href="https://forums.suse.com/forumdisplay.php?22-SUSE-Manager" target="_blank" rel="noopener noreferrer">forum</a>.</p>;`
    2. Replace `messages: []` by `messages: [previewMessage]` in the initial state assignement
4. Fix `manager/group-formula.js` and `minion-formula.js`:
    1. Remove the `saveFormula` function and the corresponding prop from `FormulaForm`
    2. Rename the `currentScope` prop to `scope`
    3. Add a `systemId` prop: `systemId={serverId}` for `minion-formula.js` and `systemId={groupId}` for `group-formula.js`
    4. Add a `saveUrl` prop: `saveUrl="/rhn/manager/api/formulas/save"`
