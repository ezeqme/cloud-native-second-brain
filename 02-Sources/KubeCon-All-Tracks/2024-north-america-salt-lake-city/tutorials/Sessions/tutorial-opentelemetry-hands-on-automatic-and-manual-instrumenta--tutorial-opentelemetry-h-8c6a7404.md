---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Tutorials"
themes: ["Observability"]
speakers: ["Tobias Angerstein", "Novatec Consulting GmbH", "Tiffany Jernigan", "Independent"]
sched_url: https://kccncna2024.sched.com/event/1i7pd/tutorial-opentelemetry-hands-on-automatic-and-manual-instrumentation-for-java-and-python-apps-tobias-angerstein-novatec-consulting-gmbh-tiffany-jernigan-independent
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+OpenTelemetry+Hands-on+-+Automatic+and+Manual+Instrumentation+for+Java+and+Python+Apps+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Tutorial: OpenTelemetry Hands-on - Automatic and Manual Instrumentation for Java and Python Apps - Tobias Angerstein, Novatec Consulting GmbH & Tiffany Jernigan, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Tutorials]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: Tobias Angerstein, Novatec Consulting GmbH, Tiffany Jernigan, Independent
- Schedule: https://kccncna2024.sched.com/event/1i7pd/tutorial-opentelemetry-hands-on-automatic-and-manual-instrumentation-for-java-and-python-apps-tobias-angerstein-novatec-consulting-gmbh-tiffany-jernigan-independent
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+OpenTelemetry+Hands-on+-+Automatic+and+Manual+Instrumentation+for+Java+and+Python+Apps+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Tutorial: OpenTelemetry Hands-on - Automatic and Manual Instrumentation for Java and Python Apps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pd/tutorial-opentelemetry-hands-on-automatic-and-manual-instrumentation-for-java-and-python-apps-tobias-angerstein-novatec-consulting-gmbh-tiffany-jernigan-independent
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+OpenTelemetry+Hands-on+-+Automatic+and+Manual+Instrumentation+for+Java+and+Python+Apps+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8CKgAyenEjo
- YouTube title: Tutorial: OpenTelemetry Hands-on - Automatic and Manual Instrumentatio... T. Angerstein, T. Jernigan
- Match score: 0.895
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tutorial-opentelemetry-hands-on-automatic-and-manual-instrumentation-f/8CKgAyenEjo.txt
- Transcript chars: 67870
- Keywords: basically, actually, method, application, python, quickly, instrumentation, little, happening, adding, internal, traces, spring, tracer, additional, everything, pretty, having

### Resumo baseado na transcript

all right uh hi everyone uh thanks for coming um I guess right after the Keynotes and on the last day so just a little cares who here has used Optometry before okay cool all right so by the title you probably figured out we're going to be talking about open Telemetry for automatic and manual instrumentation if you don't know what that means yet that is perfectly fine we'll be going into that uh who here uses Java all right and who uses python okay pretty cool all right by just also adding the user ID for instance or you want to add some custom true client IP which you get from your CDN or something like that okay so with that we've just learned what we can do with automatic instrumentation um but

### Excerpt da transcript

all right uh hi everyone uh thanks for coming um I guess right after the Keynotes and on the last day so just a little cares who here has used Optometry before okay cool all right so by the title you probably figured out we're going to be talking about open Telemetry for automatic and manual instrumentation if you don't know what that means yet that is perfectly fine we'll be going into that uh who here uses Java all right and who uses python okay pretty cool all right so yeah hi I'm Tiffany Jernigan um I do developer advocacy things such is this um I just became a cncf Ambassador like two weeks ago so this is my first cubec con after that so that's pretty cool um if you want to see what I've been up to you can just go to Tiffany f.d which is also my blue sky since a bunch of people are starting to use that now and then the QR codes are for our linkedin's and then LinkedIn and X if you use it on the bottom there and hi I'm Toby I'm a senior observability consultant at noatch a German consultancy company and I'm mainly working in the area of observability and Consulting our customers in improving their observability infrastructure also by using open Telemetry that's also the reason why I'm taking part in that um talk and before we we're going to start um yes we have some credits to some some awesome guys to Nicholas till Yan splan and also Mattias Polo who basically built uh the um open Telemetry lab for the Linux foundation so without their work we wouldn't be able to kind of provide you this talk and many thanks uh to you and also for supporting us uh in in preparing um that talk and a little fun fact we talked for the first time and met literally three weeks ago all right so this is kind of the little agenda of what we're going to start going over today so kind of give a little overview of things with open Telemetry uh there's going to be multiple demos um so we're just going to be going through things pretty much live here so we'll see how that goes um so there's a bunch of different things for if you want to go and follow along um so we want there's only two of us obviously so we can't come along and try helping people so it's kind of up to you if you want to do as well um basically there's a new Linux Foundation uh training course uh so that's the one on left there you may have also seen them today that there is a new open Telemetry certification and this is free so that's cool and then the one on the right is also linked in the other one but it's the
