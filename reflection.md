# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**
- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

Three core actions a user should be able to perform are:
- Add a pet and owner information so the app can personalize care planning.
- Create and edit pet care tasks like walks, feeding, medications, and enrichment.
- Generate and view today's scheduled tasks with priorities and timing clearly displayed.

The initial UML design uses a small domain model aligned to the pet care planning workflow.
- `Owner` stores the pet owner’s name, preferences, and daily availability. It is responsible for checking whether a task fits the owner's schedule and providing a summary of owner constraints.
- `Pet` stores the pet’s name, species, age, and care requirements. It is responsible for capturing pet-specific needs and determining whether a task is appropriate for this pet.
- `Task` represents an individual care item with title, duration, priority, category, and optional recurrence. It is responsible for task-level behavior like determining priority, formatting labels for display, and matching task categories.
- `Schedule` holds the selected tasks for a day, tracks total duration, and stores explanatory notes. It is responsible for adding/removing tasks, sorting them by time, and producing a summary or explanation of the plan.
- `Scheduler` uses the owner, pet, and task list to build the daily care plan. It is responsible for filtering tasks by constraints, ranking them by priority, assigning times, generating the final schedule, and validating the result.


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

During implementation I refined the model based on a review of the class skeleton. I added an explicit `Owner.pets` relationship so the ownership model is clear, and I introduced a `ScheduledItem` class so a `Schedule` can store tasks with assigned start times instead of only raw task objects. This change was made to reduce logic complexity and support real scheduling behavior more naturally.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
