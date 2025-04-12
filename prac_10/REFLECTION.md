# CP1404 Practical Reflection

Write short but thoughtful answers to each of the following.  
Replace each `...` with your meaningful answer.

## Estimates

### How was your estimate accuracy usually?

My estimates were not always accurate at the beginning. I tended to underestimate how long it would take to debug or properly configure Flask, especially when running into issues like import errors or missing packages.

### How did your estimate accuracy improve or change during the course of the subject?

As I worked on more practicals and encountered recurring problems (e.g., missing templates, incorrect file names, GitHub linking), I became more realistic in my time estimates. I also became better at anticipating setup time and test/debug cycles.

### What did you learn from doing these estimates?

I learned that estimating programming tasks is a skill that improves with experience. I now consider potential problems, like debugging or refactoring, as part of my estimation process instead of just coding time.

## Code Reviews

### What have you learned from being reviewed by other people?

I learned to be more mindful of code readability and structure. Sometimes others pointed out things I thought were clear but were not to them, which helped me improve my naming and organization.

### What have you learned from doing code reviews of other people?

Reviewing others' code helped me reflect on my own coding habits. I could spot better ways to structure Flask routes, write comments, or improve variable names by reading someone else’s work objectively.

Provide proper Markdown links (not bare URLs) to two (2) PRs that show you doing good code reviews for any of the past pracs.  
For each one, write a short explanation of what was good about your review.

### Good Code Review 1

[Review on Flask Basic Project](https://github.com/jc959024/CP1404-prac/tree/main/prac_10/flaskProject)

### Explanation

In this review, I provided suggestions on using `render_template` for better maintainability instead of returning raw HTML strings. I also pointed out a variable naming inconsistency and suggested reusing a temperature conversion function.

### Good Code Review 2

[Review on Flask + Wiki Project](https://github.com/jc959024/flaskdemo)

### Explanation

I reviewed the handling of disambiguation and page errors in the Wikipedia search route. I also recommended using Jinja template blocks correctly to avoid HTML repetition and make the layout cleaner.

## Practicals

### Regarding the **practical tasks** overall, what would you change if you were in charge of the subject?

I would include a clearer explanation of how to distinguish between local files and external libraries when using `import`, especially when students accidentally install third-party libraries with the same name as their files (like `temperature`). I would also include a tutorial on uploading projects to GitHub for beginners.

### What did you do really well for practicals in this subject?

I persisted through debugging and solved multiple issues including Flask import errors, local module conflicts, and how to integrate Wikipedia API with route templates. I also created a well-structured Flask project with clean navigation and reusable templates, and I successfully pushed it to GitHub with meaningful commit messages.

