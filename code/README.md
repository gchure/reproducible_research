# `code`

It's important to keep the code that is executed separated from that which is called. The distinct difference here is that executed code should change from day-to-day or analysis to analysis. You're not necessarily making all measurements at the same time, or at the exact same concentration, or even on the same materials. As your experiments change, your code should also change to make sure you a transforming or interpreting the data correctly. 

However, any code that is critical for an analysis, such as a function that computes some quantity from your data, should be written such that it is *modular* and is used the same way from day-to-day. This type of code should be referenced by your analysis or processing scripts such that if you change the way you perform something, it can be applied to all of your experiments simply by rerunning the processing scripts. You *don't* want to go back through each experiment and make that change by hand.

This directory is broken into several subdirectories, each of which has a `README.md` file describing what should be there with some examples. 