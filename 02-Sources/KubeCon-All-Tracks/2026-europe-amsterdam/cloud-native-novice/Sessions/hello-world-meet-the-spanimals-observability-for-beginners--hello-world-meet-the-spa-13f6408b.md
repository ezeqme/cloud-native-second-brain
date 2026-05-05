---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Cloud Native Novice"
themes: ["Observability"]
speakers: ["Tiffany Jernigan", "Grafana Labs", "Matthias Haeussler", "CGI"]
sched_url: https://kccnceu2026.sched.com/event/2CW2F/hello-world-meet-the-spanimals-observability-for-beginners-tiffany-jernigan-grafana-labs-matthias-haeussler-cgi
youtube_search_url: https://www.youtube.com/results?search_query=Hello+World%2C+Meet+the+Spanimals%3A+Observability+for+Beginners+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Hello World, Meet the Spanimals: Observability for Beginners - Tiffany Jernigan, Grafana Labs & Matthias Haeussler, CGI

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Tiffany Jernigan, Grafana Labs, Matthias Haeussler, CGI
- Schedule: https://kccnceu2026.sched.com/event/2CW2F/hello-world-meet-the-spanimals-observability-for-beginners-tiffany-jernigan-grafana-labs-matthias-haeussler-cgi
- Busca YouTube: https://www.youtube.com/results?search_query=Hello+World%2C+Meet+the+Spanimals%3A+Observability+for+Beginners+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Hello World, Meet the Spanimals: Observability for Beginners.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW2F/hello-world-meet-the-spanimals-observability-for-beginners-tiffany-jernigan-grafana-labs-matthias-haeussler-cgi
- YouTube search: https://www.youtube.com/results?search_query=Hello+World%2C+Meet+the+Spanimals%3A+Observability+for+Beginners+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_bLAN_mzxIs
- YouTube title: Hello World, Meet the Spanimals: Observability for Beginners - Tiffany Jernigan & Matthias Haeussler
- Match score: 0.843
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/hello-world-meet-the-spanimals-observability-for-beginners/_bLAN_mzxIs.txt
- Transcript chars: 30617
- Keywords: basically, metrics, logs, traces, application, actually, little, generator, database, information, taking, within, observability, talking, together, animal, signals, generate

### Resumo baseado na transcript

Um, if you who out of curiosity, who here is like a beginner or newer to observability? So, I'm definitely curious as to like what people's thoughts are afterwards and if they have ideas that, oh, you should have done this because people have opinions in many spaces and this is one of them. So now, right now we've seen something to do with like metrics, we've seen logs, we've seen traces. This is more distributed tracing is more we had under the umbrella for Tracy. So um as we mentioned traces or tracy do kind of the end to end journey where whereas the spannies are like the breakdowns in the in the middle element metrics for the for the metrical part for trends and rates and and all the We kind of built a a demo application that we going to look into in a moment and trying to like walk through all the various signals that we're just covering now.

### Excerpt da transcript

Hi everyone. Um, welcome to our talk. Um, if you who out of curiosity, who here is like a beginner or newer to observability? Okay. So, maybe less than half the room. So, I'm definitely curious as to like what people's thoughts are afterwards and if they have ideas that, oh, you should have done this because people have opinions in many spaces and this is one of them. But yeah, so basically as you can tell from the screen, um we're going to be talking about more of the like intro level things of observability. So yeah, hi, I'm Tiffany Jernigan. Um I am a developer advocate at Graphana Labs. Um hi, I'm Matias. I'm a VP expert at at CGI. And um we've just made the discovery that we've pretty much been in this very room exactly three years ago. So this is where we did our first talk together. And I think we should take this photo again. Don't you think as well? So come our guests. >> All right. So now back to the topic. Now we know it's just right after lunch and people sometimes are a bit um um it's a bit harder to like concentrate and focus.

So we we start with a little game. Tiffany's just asked um who is new to the part of obsibility. Who in here is already experienced in observability? Okay. And who is not going to raise their hand no matter what I'm going to ask. Okay, good. Uh I just wanted to check if you're all there. So now we're going to do a little interactive game. The first of the round we um I'm going to play directly with Tiffany and then I want you to interact and those with some more background in observability are definitely uh invited to answer. So, um, Tiffany, um, what do you think who that is? >> I think that's Tracy. >> That is Tracy. Correct. So, um, as I said, we're going to do a light introduction before we go into the more technical uh, deeper topics. So, this is Tracy. And if you if you know Tracy by now, you should also know that Tracy is not coming along alone. Tracy is coming along with a couple of spannies which are kind of like similar to Tracy like little Tracy's um and they're normally coming around together.

So what Tracy does it's it's basically she's jumping from one point in a large leap to the other while the spannies normally take like smaller leaps um and like the compost uh jumps off the um of the spannies is basically what the trace you can do in one step. So now we're going to go for the next round. >> Okay. So now that you kind of have an idea of how this game works, do people want to try the guessing the name
