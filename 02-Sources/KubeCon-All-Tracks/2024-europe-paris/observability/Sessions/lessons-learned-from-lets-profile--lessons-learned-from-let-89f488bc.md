---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Observability"
themes: ["Observability"]
speakers: ["Frederic Branczyk", "Polar Signals"]
sched_url: https://kccnceu2024.sched.com/event/1YePX/lessons-learned-from-lets-profile-frederic-branczyk-polar-signals
youtube_search_url: https://www.youtube.com/results?search_query=Lessons+Learned+from+Let%27s+Profile+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Lessons Learned from Let's Profile - Frederic Branczyk, Polar Signals

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: France / Paris
- Speakers: Frederic Branczyk, Polar Signals
- Schedule: https://kccnceu2024.sched.com/event/1YePX/lessons-learned-from-lets-profile-frederic-branczyk-polar-signals
- Busca YouTube: https://www.youtube.com/results?search_query=Lessons+Learned+from+Let%27s+Profile+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Lessons Learned from Let's Profile.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePX/lessons-learned-from-lets-profile-frederic-branczyk-polar-signals
- YouTube search: https://www.youtube.com/results?search_query=Lessons+Learned+from+Let%27s+Profile+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gRT_tVVizk4
- YouTube title: Lessons Learned from Let's Profile - Frederic Branczyk, Polar Signals
- Match score: 0.753
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/lessons-learned-from-lets-profile/gRT_tVVizk4.txt
- Transcript chars: 23133
- Keywords: actually, basically, profiling, function, compiler, optimize, production, allocations, question, profile, already, container, always, probably, resources, benchmark, memory, inlining

### Resumo baseado na transcript

before we get to the meat of uh this presentation I want to kind of set the scene a little bit um and uh kind of frame where we are in Computing history so let's go back a little bit to 1971 and Intel writes Computing history by releasing the first commercially produced U microprocessor the Intel 44 um and this was like I said pretty significant because it was the first commercially produced um microprocessor and didn't stop there they uh you know as we all know kept uh

### Excerpt da transcript

before we get to the meat of uh this presentation I want to kind of set the scene a little bit um and uh kind of frame where we are in Computing history so let's go back a little bit to 1971 and Intel writes Computing history by releasing the first commercially produced U microprocessor the Intel 44 um and this was like I said pretty significant because it was the first commercially produced um microprocessor and didn't stop there they uh you know as we all know kept uh producing more and more chips and just in those 3 years between um the 4004 and the 8080 they more than doubled the number of transistors in um in these chips um just a few years after that again uh you know they produced one of the most um Infamous um chips ever produced the 86 with 29,000 transistors um you probably already understand where I'm going with with this this is something that one of the Intel co-founders Gordon Moore coined as U Mo's law initially he said every every year the number of transistors are going to double eventually he kind of retracted that statement and said okay maybe only every two years but basically throughout Computing history so far this pretty much um held true um more or less until now um last year Apple gave a really cool keynote um when they were releasing the M2 Chip where they using this is kind of a marketing term the 5 nanometer uh technology nothing's actually 5 nanometers in this stuff um they're actually the but they made a really interesting statement in this keynote they said some of the components in these chips are now 12 nanometers wide um and the reason uh this is important is uh we have known physical limits of how small we think transistors can get you know unless there's a completely new breakthrough and we may not be producing silicon chips at all anymore and a single silicon chip a single silicon atom is what we think is the theoretical physical limits of how small we can make a single transistor and so you know going um after more law assuming that we can actually still economically uh produce chips that go get smaller and smaller we're still pretty close actually to you know the physical limits um known known to us and so uh that means you know at least the way that we know Morse law it is definitely ending however um my thesis is basically um Long Live mors law although not in the way you know that it originally was uh stated and basically the way I think uh Computing history is going to continue from this point onwards is in two wa
