---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Security + Identity + Policy"
themes: ["Security"]
speakers: ["David Korczynski", "Adam Korczynski", "Ada Logics"]
sched_url: https://kccncna2022.sched.com/event/1BvfI/fuzzing-session-finding-bugs-and-vulnerabilities-automatically-david-korczynski-adam-korczynski-ada-logics
youtube_search_url: https://www.youtube.com/results?search_query=Fuzzing+Session%3A+Finding+Bugs+and+Vulnerabilities+Automatically+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Fuzzing Session: Finding Bugs and Vulnerabilities Automatically - David Korczynski & Adam Korczynski, Ada Logics

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]]
- País/cidade: United States / Detroit
- Speakers: David Korczynski, Adam Korczynski, Ada Logics
- Schedule: https://kccncna2022.sched.com/event/1BvfI/fuzzing-session-finding-bugs-and-vulnerabilities-automatically-david-korczynski-adam-korczynski-ada-logics
- Busca YouTube: https://www.youtube.com/results?search_query=Fuzzing+Session%3A+Finding+Bugs+and+Vulnerabilities+Automatically+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Fuzzing Session: Finding Bugs and Vulnerabilities Automatically.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/1BvfI/fuzzing-session-finding-bugs-and-vulnerabilities-automatically-david-korczynski-adam-korczynski-ada-logics
- YouTube search: https://www.youtube.com/results?search_query=Fuzzing+Session%3A+Finding+Bugs+and+Vulnerabilities+Automatically+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DSJePjhBN5E
- YouTube title: Fuzzing Session: Finding Bugs and Vulnerabilities Automatically - David Korczynski & Adam Korczynski
- Match score: 0.87
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/fuzzing-session-finding-bugs-and-vulnerabilities-automatically/DSJePjhBN5E.txt
- Transcript chars: 32249
- Keywords: projects, issues, fasting, memory, fussing, forcing, forces, languages, actually, security, write, function, target, strings, second, string, writing, fossils

### Resumo baseado na transcript

uh so welcome to this talk uh fussing finding bugs and vulnerabilities automatically I'm David and this is Adam and we're from a niche company called ideologix where we specialize in various forms of Advanced software security uh topics and the way that we are presenting in this talk is mainly work we have done in collaboration with the coordinating Computing Foundation and effectively what we will talk about is how we manage to fuss a lot of cncf projects bit about what the results were and that's kind of

### Excerpt da transcript

uh so welcome to this talk uh fussing finding bugs and vulnerabilities automatically I'm David and this is Adam and we're from a niche company called ideologix where we specialize in various forms of Advanced software security uh topics and the way that we are presenting in this talk is mainly work we have done in collaboration with the coordinating Computing Foundation and effectively what we will talk about is how we manage to fuss a lot of cncf projects bit about what the results were and that's kind of it so I'll let Adam Adam yeah so we have been forcing a bunch of the graduated and incubating projects in the cncf landscape and including these ones I believe there are a few missing for example istio but but these projects are all being fast and so what we have done is we'll go into this later but but we have taken a bunch of the amazing open source capabilities into enforcing and brought this into these projects in various ways um and each project has been different in our approach because the projects are so different in nature but uh part of this talk is to present that forcing works for so many different types of projects including these ones here and that that even includes different languages as well so the projects are different in nature some of them are like well I don't know if any of these are necessary libraries maybe home has some but they are very different in nature but also different in architecture so like language is different and and so on so agenda what is fussing why do we fast how do we fast and then we're going to present a case study focused on HDL so in the in in very general terms fasting is a way to automate test case generation and that's kind of the origins of it and what it is in practice as well from a more pragmatic perspective is a way to find books and software or a way to ensure that there's no boxing software and um around 10 so passing is a technique that was used maybe maybe introduced sorry 20 years ago or so but around a decade ago 10 years ago maybe a little bit more there came this uh Improvement in fasting which is coverage based feedback driven flossing which essentially relies on instrumenting the target program in a certain way observing how the target program behaves and kind of driving this automated test case generation based on what You observe in the Target program so fussing is often referred to as throwing a lot of random stuff at a program whereas these days it's more like accurately described as li
