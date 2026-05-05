---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Charlie Egan", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFwy/project-lightning-talk-how-to-add-a-new-language-feature-to-opa-charlie-egan-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+How+To+Add+A+New+Language+Feature+To+OPA+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: How To Add A New Language Feature To OPA - Charlie Egan, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Charlie Egan, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFwy/project-lightning-talk-how-to-add-a-new-language-feature-to-opa-charlie-egan-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+How+To+Add+A+New+Language+Feature+To+OPA+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: How To Add A New Language Feature To OPA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFwy/project-lightning-talk-how-to-add-a-new-language-feature-to-opa-charlie-egan-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+How+To+Add+A+New+Language+Feature+To+OPA+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gPpHTVxHEKQ
- YouTube title: Project Lightning Talk: How To Add A New Language Feature To OPA - Charlie Egan, Maintainer
- Match score: 0.92
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-how-to-add-a-new-language-feature-to-opa/gPpHTVxHEKQ.txt
- Transcript chars: 5715
- Keywords: string, policy, language, interpolation, interpolated, called, template, feature, responsible, update, tokens, compiler, written, policies, changes, within, username, related

### Resumo baseado na transcript

So uh if you are not familiar with our project, it's a general purpose policy engine. Sometimes people might ask us and even if you've not used our project, you've probably written policies in another language if not ours. Um, all language changes have a cost and we'll see a little bit more about that shortly.

### Excerpt da transcript

Yeah. Hello everybody. Um I'm Charlie from the OPER project. So uh if you are not familiar with our project, it's a general purpose policy engine. It's uh what could you do with a general purpose policy engine? Sometimes people might ask us and even if you've not used our project, you've probably written policies in another language if not ours. So whether a particular runner can deploy to a given environment or who can make changes to uh a particular path or directory within a git repo. These are the kinds of things that you can express with policies and they're the kinds of things that we hope that you might express with our policy policy language called rego. Uh the way that you use oper is you take some policy code that you've written. You load it into an instance of open policy agent and um then you provide structured information form of JSON. Uh Opera then evaluates your policy with that information in mind and produces a decision result for you. So OP is responsible for making decisions based on your policy.

It's also responsible for reloading your policy as it changes and producing audit logs as well. So we we've been trying to make Rego um easier for people to get started with and more familiar to them. Um so imagine you wanted to write a policy which uh you've got you got a a user and they don't have the rules that are required and you want to return a message saying that this username um doesn't have um uh it doesn't have a role that's allowed. Previously uh you would need to handle the case where the username was undefined and you would need to use sprint f to build a string using formatting directives. Um the username undefined handling was not explicitly related to your policy. And so we've tried to make uh tried to make this better with a new feature called string interpolation. Uh this same policy uh would look like this now. Uh so we have a new string interpolation syntax. And I'm going to talk briefly about how we've added that in OpE 1.12. We thought a long time about whether or not we should add this feature.

Um, all language changes have a cost and we'll see a little bit more about that shortly. The first thing that you have to do if you want to make a change to our policy language is to update the parser. Uh, the parser is responsible for scanning um raw source code and breaking it down into different tokens. Uh, we added two new tokens as part of this work. Um the first part is um any part of a string interpolated a string interpol
