# OPA-Lang

Repetitive Strain Injures (RSI) are common occupational diseases among developers due to long periods spent sitting, typing and clicking. Dictating code using speech recognition engines is a compelling alternative to alleviate RSI  among programmers. However, dictating code in natural human languages is long and tedious. A viable solution is to find abbreviations to make dictation shorter, faster and less fatiguing. Unfortunately this imposes yet other challenges, as existing speech recognitions engines require dictionaries to learn the abbreviations. Then, these abbreviations should sound different to reduce recognition mistakes. If we add to this the numerous programming languages existing today and the phonetic differences between programmers around the world (as some abbreviations may be easy to pronounce for some, but difficult for others) we end up with a problem that requires automation.


For example, take the following java loop:

`for (int x = 0; x < N; x++) {}`

In English, this loop is read:
*for open parenthesis integer ex equals zero semicolon ex minor than n semicolon ex plus plus close parenthesis open bracket close bracket*. 

Such long sentences will quickly provoke fatigue in the programmer and compels her to abandon the attempt to dictate code. Using abbreviations this code may be read:

*for opa int ex ecu zero semi x le en semi x papa apo ribket leftket* 

Certainly sound like a lot of gibberish, but have you forget how the code looked to you the first time you saw it? 

OPA-Lang is a tool to find abbreviation that can be used by programmers all over the world to dictate code. The tool takes three inputs to  generate a set of abbreviations that can be used to dictate a programming language using an speech recognition engine:

- The syntax and semantics of a programing language.
- A confusion matrix describing the likelihood that a phoneme is confused by other.
- A dictionary of the natural human language of the programmer that is going to dictate.
  
OPA-Lang uses these inputs to generate a set of abbreviations that:
- Cover all the language constructs
- Have a reduced probability of being confused among each other
- Are easy to pronounce by the programmer.

The name came from the an abbreviation of “Open PArenthesis” (OPA).
