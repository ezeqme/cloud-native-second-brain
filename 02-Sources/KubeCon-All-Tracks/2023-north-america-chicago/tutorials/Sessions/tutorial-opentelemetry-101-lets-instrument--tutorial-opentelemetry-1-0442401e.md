---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Tutorials"
themes: ["AI ML", "Observability"]
speakers: ["Paige Cruz", "Chronosphere"]
sched_url: https://kccncna2023.sched.com/event/1R2sI/tutorial-opentelemetry-101-lets-instrument-paige-cruz-chronosphere
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+OpenTelemetry+101%3A+Let%27s+Instrument%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Tutorial: OpenTelemetry 101: Let's Instrument! - Paige Cruz, Chronosphere

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Tutorials]]
- Temas: [[AI ML]], [[Observability]]
- País/cidade: United States / Chicago
- Speakers: Paige Cruz, Chronosphere
- Schedule: https://kccncna2023.sched.com/event/1R2sI/tutorial-opentelemetry-101-lets-instrument-paige-cruz-chronosphere
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+OpenTelemetry+101%3A+Let%27s+Instrument%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Tutorial: OpenTelemetry 101: Let's Instrument!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2sI/tutorial-opentelemetry-101-lets-instrument-paige-cruz-chronosphere
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+OpenTelemetry+101%3A+Let%27s+Instrument%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CB2nEcnBBcE
- YouTube title: Tutorial: OpenTelemetry 101: Let's Instrument! - Paige Cruz, Chronosphere
- Match score: 0.858
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/tutorial-opentelemetry-101-lets-instrument/CB2nEcnBBcE.txt
- Transcript chars: 66922
- Keywords: instrumentation, trace, traces, otel, little, request, programmatic, requests, manually, instrument, instrumenting, search, working, python, manual, whatever, running, helpful

### Resumo baseado na transcript

hello everybody uh it's 4:30 I figure it's time we can get started um if you're coming on in grab a seat this is open Telemetry 101 let's instrument specifically for traces today is sort of a observability 101 and a tracing 101 uh the most important thing to know at the top is all of these slides are available you can uh if you don't trust QR codes there's a bitly link for you um no worries this Workshop will be available after cubec con so if you are Host 16686 you don't have to select H otel from the menu um but Jer also instruments itself so you will see jger query pop up as a service we really care about hello otel spans so maybe just go ahead and select hello otel is people's first steps with tracing instrumentation where they just need to add a key value pair span attribute um they're just metadata to annotate a span with just more information that might help you the uh sort of API call is span do set kind and it says server which reflects that this span was generated from flask's point of view our application and so again we don't know how much time we spent waiting on the dog API maybe they had problems maybe they pushed out really buggy what we're going to see when we click in to our Trace view is Boom you see this little thing that says logs all of a sudden we've got this span event that shows up as logs um with a Tim stamp that time stamp

### Excerpt da transcript

hello everybody uh it's 4:30 I figure it's time we can get started um if you're coming on in grab a seat this is open Telemetry 101 let's instrument specifically for traces today is sort of a observability 101 and a tracing 101 uh the most important thing to know at the top is all of these slides are available you can uh if you don't trust QR codes there's a bitly link for you um no worries this Workshop will be available after cubec con so if you are running out of power um and your laptop dies there's something within Network um you can't grab podman and time whatever it takes um you can access this workshop at any time free of charge um extend it modify it for your use case um so no worries take this workshop at your own pace um and I'll leave this up for a couple more minutes as people are finding their seats but thank you all for coming it's really lovely to see so much interest in otel and tracing it's my favorite Telemetry type and I'm excited to share it with you today I have with me two helpers right over there if they can raise their hands stand up if you are working on the workshop and you get stuck um raise your hand and uh one of them or me will come over and see if we can debug and help you out the way this Workshop will go is I'll present some content we've got about five labs um but this is sort of a work at your own pace so if you want to skip ahead or there's stuff you already know it's really for your benefit and your learning all right we got a couple more people finding their seats welcome welcome okay the second thing that is important to know other than the QR code is there are a few prere that uh you may want to get started downloading one of of which is podman if you haven't heard of it is a alternative to Docker there's a lot of other use cases for it um but that is what this Workshop is set up so um grab a link to podman uh download it for your system Python 3 um we'll be working on a Python 3 application um and then I should have added a comma here Python 3 is one dependency and then the sample application the repo is another so while folks are streaming in make sure you've got those three setup um and if the Wi-Fi is a little iffy you've got there's one whole intro to observability so you can kind of keep retrying all right okay we'll take things away so um if you have this loaded on your laptop I kind of recommend having one window with the slide deck and one window with your editor um or another browser um this is sort of how
