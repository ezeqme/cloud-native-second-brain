---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Joel Speed", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1i7nv/exceeded-your-validation-cost-budget-now-what-joel-speed-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Exceeded+Your+Validation+Cost+Budget%3F+Now+What%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Exceeded Your Validation Cost Budget? Now What? - Joel Speed, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Salt Lake City
- Speakers: Joel Speed, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1i7nv/exceeded-your-validation-cost-budget-now-what-joel-speed-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Exceeded+Your+Validation+Cost+Budget%3F+Now+What%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Exceeded Your Validation Cost Budget? Now What?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nv/exceeded-your-validation-cost-budget-now-what-joel-speed-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Exceeded+Your+Validation+Cost+Budget%3F+Now+What%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IfaPAqDfJHk
- YouTube title: Exceeded Your Validation Cost Budget? Now What? - Joel Speed, Red Hat
- Match score: 0.906
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/exceeded-your-validation-cost-budget-now-what/IfaPAqDfJHk.txt
- Transcript chars: 23029
- Keywords: cost, length, string, validation, schema, budget, million, server, formula, cardinality, anyone, validations, within, actually, request, minimum, working, traversal

### Resumo baseado na transcript

okay uh welcome folks uh today we're going to be looking at Cost validation budgets or validation cost budgets I should say uh within cell in kubernetes and what they mean and in particular why why they might error and how to avoid that so what we're going to look at today we'll start off by taking a look at what cell is and working out why we might actually want to use that feature uh we'll talk about what and why we have these validation cost budgets we'll start be the cheaper option but to do this the rule cost would either have to be incredibly high or the calculat cardinality would have to be incredibly low and to get that you'd have to have a massive massive object with lots of required Fields

### Excerpt da transcript

okay uh welcome folks uh today we're going to be looking at Cost validation budgets or validation cost budgets I should say uh within cell in kubernetes and what they mean and in particular why why they might error and how to avoid that so what we're going to look at today we'll start off by taking a look at what cell is and working out why we might actually want to use that feature uh we'll talk about what and why we have these validation cost budgets we'll start looking at the rule cost and cardinality two elements of the total cost and then we'll finish up by making sure that we all understand how to avoid high cost validations uh High validation costs in our crds uh before we go too far though I'm Joel I'm a principal software engineer at Red Hat I focus primarily on cloud technology CCMS and cppy uh but I'm also one of our open shift API review team and last year contributed a library as part of the cell project Upstream so what is cell well it's this thing called the common expression language and it came out of Google the idea was to create something simple that would be able to be used for kind of common Expressions uh that could then be embedded into other projects so the idea was that it would be SE like non-t incomplete deliberately so that it's not too complex lightweight fast execution and ideally extensible meaning that not only do you have the built-in syntax of the language but we can start adding new functions on top of the language to make it more usable in specific use cases the bottom box here the sort of dark box with the green text is an example of of a cell expression account and transaction are objects they have Fields within them we've got operators that you'll probably recognize and this condition evaluates to a Boolean true or false now this started being used in Cube for crd validation so ex kubernetes validations we brought that in GA in 129 and that the idea here was basically to make crds more self-contained and easier to M easier to develop the idea is that we can BR bring complex validation into the C schema have it execute within the API server and get rid of web hooks uh an example of this is this immutable field schema this is quite common uh across apis where you have some data and you don't want it to be changed with cell all I have to do is write self equals old self and that's solve for me that data can no longer be changed once it's set in that API it's also used in other places uh one of which is validating admissi
