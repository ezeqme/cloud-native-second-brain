---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["Security"]
speakers: ["Adam", "David Korczynski", "Ada Logics"]
sched_url: https://kccncna2023.sched.com/event/1TxW4/security-hub-fuzzing-introduction-+-oss-fuzz-demo-adam-david-korczynski-ada-logics
youtube_search_url: https://www.youtube.com/results?search_query=SECURITY+HUB%3A+Fuzzing+Introduction+%2B+OSS-Fuzz+Demo+CNCF+KubeCon+2023
slides: []
status: parsed
---

# SECURITY HUB: Fuzzing Introduction + OSS-Fuzz Demo - Adam & David Korczynski, Ada Logics

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Chicago
- Speakers: Adam, David Korczynski, Ada Logics
- Schedule: https://kccncna2023.sched.com/event/1TxW4/security-hub-fuzzing-introduction-+-oss-fuzz-demo-adam-david-korczynski-ada-logics
- Busca YouTube: https://www.youtube.com/results?search_query=SECURITY+HUB%3A+Fuzzing+Introduction+%2B+OSS-Fuzz+Demo+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre SECURITY HUB: Fuzzing Introduction + OSS-Fuzz Demo.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1TxW4/security-hub-fuzzing-introduction-+-oss-fuzz-demo-adam-david-korczynski-ada-logics
- YouTube search: https://www.youtube.com/results?search_query=SECURITY+HUB%3A+Fuzzing+Introduction+%2B+OSS-Fuzz+Demo+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=g-LQGF6wOrQ
- YouTube title: SECURITY HUB: Fuzzing Introduction + OSS-Fuzz Demo - Adam & David Korczynski, Ada Logics
- Match score: 0.82
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/security-hub-fuzzing-introduction-oss-fuzz-demo/g-LQGF6wOrQ.txt
- Transcript chars: 28261
- Keywords: fussing, continuously, engine, report, projects, repository, harness, coverage, write, running, complex, issues, testing, component, actually, source, written, various

### Resumo baseado na transcript

thank you for coming to this fing session of the security uh track of uh cucon Chicago 2023 this is uh first introduction and OSS first demo uh my name is Adam kachinski this is David we are from ad Logics and we do a lot of fing in general and a lot of fing on of cntf projects um and this is more of a practical approach to f um and should have a lot of we we have a lot of examples and uh uh practical how tos

### Excerpt da transcript

thank you for coming to this fing session of the security uh track of uh cucon Chicago 2023 this is uh first introduction and OSS first demo uh my name is Adam kachinski this is David we are from ad Logics and we do a lot of fing in general and a lot of fing on of cntf projects um and this is more of a practical approach to f um and should have a lot of we we have a lot of examples and uh uh practical how tos to get started and to to get started with fussing and triing your findings Etc the agenda we'll talk about the the cncf fing ecosystem there are a lot of uh there's a lot of stuff going on for the cstf projects specifically um but there are a lot of resources and materials available for for uh the open source uh Community as a whole um so if you're not a cncf project this is also for you uh then uh we'll do do a little intro on how to force a software software project um uh yeah I'll I'll leave um I'll I'll get we'll get to that in a second uh and then the fing live cycle so what what happens when you have written a fer what do you do what and how do you do it efficiently uh and OSS for finally um which is a big part of the the fing life cycle um so yeah uh fussing as a concept is a way to in essence stress test applications and by and large the goal is to find uh bugs both security and reliability issues and the goal is to because it's stress testing we are working with Dynamic analysis here mean we actually execute the code on the analysis so what you are doing when you're are fussing is you are developing a fusser and this fer will call your application essentially infinitely meaning it will just run forever either until it stops or until it finds a bug or so and when I say it stops I mean when someone stops it uh so it's just a process of stress testing your application over and over again and in general the fussing uh approach that that that we use which is coverage guided fussing becomes better over time when analyzing a spe specific Target and this is because it relies on what we call like genetic mutational algorithms that builds up a set of test cases where each test case represents kind of represents a an input that will execute a unique code path in the Target project relative to the other test cases that the first has generated so that's kind of like the the short story I don't want to go into too many of the of the conceptual details of fussing but the goal is to find bucks find vulnerabilities so perhaps importantly to say here it's not
