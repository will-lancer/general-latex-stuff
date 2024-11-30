This is my lab template for a junior year physics lab;
in my specific case, this is PHY 335 at Stony Brook University.
It's more or less just my basic LaTeX template, with some
goodies added by James Cross and myself.

Some specific notes and basic things that you should know
if you haven't written lab reports before:
  * To typeset units, use $\si{\delimiter\unitname}$, e.g. $\si{\milli\volt}$
    or $\si{\mega\ohm}$.
  * All figures and tables follow the same basic template
    (note that [H] in the declaration of the figures/tables;
    this is essential. It's the thing that puts the table where
    you want it to go, i.e. it doesn't let it float), e.g.:

For figures (the \textwidth thing should be changed to whatever
fits at the time),

\begin{figure}[H]
  \centering
  \includegraphics[width=0.8\textwidth]{Path/figurename.jpeg}
  \caption{Caption.}
\end{figure}

For tables,

\begin{table}[H]
  \centering
  \begin{tabluar}{|c|c|c|}
  \hline
  C11 & C12 & C13\\
  \hline
  C21 & C22 & C23\\
  C31 & C32 & C33\\
  \hline
  \end{tabular}
  \caption{Caption.}
\end{table}

  * I personally use \vocab{} to highlight certain words in
    my introduction, mainly to make it easier for the TA to
    grade it. I use it on the words mentioned in the ``Mini-lecture
    topics'' section of the questions for 335.
  * Use the align environment for equations and the like; if
    you're not citing an equation, use align*. Use \label{}
    and \ref{} to respectively label and cite things.
  * When you're writing lab reports, it takes time,
    and you're going to write it in multiple passes;
    to make sure you remember to put everything down,
    I'd recommend using \note{} to put reminders for
    what you have left to finish.
  * Use [this](https://www.tablesgenerator.com) website to typeset your LaTeX tables
    (put vertical lines in your table by pressing
    Table > Add vertical borders. It looks nicer);
    I would also liberally use ChatGPT in your data
    analysis (it's quite helpful). Another useful
    fact is that you can copy and paste directly
    from a Google Sheet into the website mentioned
    previously.






