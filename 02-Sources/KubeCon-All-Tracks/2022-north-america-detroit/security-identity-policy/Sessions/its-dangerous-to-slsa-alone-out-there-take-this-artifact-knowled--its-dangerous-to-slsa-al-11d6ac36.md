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
themes: ["AI ML", "Security"]
speakers: ["Mihai Maruseac", "Google", "Michael Lieberman", "Independent"]
sched_url: https://kccncna2022.sched.com/event/182Jr/its-dangerous-to-slsa-alone-out-there-take-this-artifact-knowledge-graph-mihai-maruseac-google-michael-lieberman-independent
youtube_search_url: https://www.youtube.com/results?search_query=It%27s+Dangerous+To+SLSA+Alone+Out+There%21+Take+This+Artifact+Knowledge+Graph%21+CNCF+KubeCon+2022
slides: []
status: parsed
---

# It's Dangerous To SLSA Alone Out There! Take This Artifact Knowledge Graph! - Mihai Maruseac, Google & Michael Lieberman, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Detroit
- Speakers: Mihai Maruseac, Google, Michael Lieberman, Independent
- Schedule: https://kccncna2022.sched.com/event/182Jr/its-dangerous-to-slsa-alone-out-there-take-this-artifact-knowledge-graph-mihai-maruseac-google-michael-lieberman-independent
- Busca YouTube: https://www.youtube.com/results?search_query=It%27s+Dangerous+To+SLSA+Alone+Out+There%21+Take+This+Artifact+Knowledge+Graph%21+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre It's Dangerous To SLSA Alone Out There! Take This Artifact Knowledge Graph!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Jr/its-dangerous-to-slsa-alone-out-there-take-this-artifact-knowledge-graph-mihai-maruseac-google-michael-lieberman-independent
- YouTube search: https://www.youtube.com/results?search_query=It%27s+Dangerous+To+SLSA+Alone+Out+There%21+Take+This+Artifact+Knowledge+Graph%21+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xFRNgIEzbkA
- YouTube title: It's Dangerous To SLSA Alone Out There! Take This Artifact... - Mihai Maruseac & Michael Lieberman
- Match score: 0.8
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/its-dangerous-to-slsa-alone-out-there-take-this-artifact-knowledge-gra/xFRNgIEzbkA.txt
- Transcript chars: 29550
- Keywords: documents, package, actually, information, another, s-bomb, ingest, little, artifacts, metadata, queries, container, packages, looking, dependencies, attestations, artifact, supply

### Resumo baseado na transcript

all right so uh we're going to be talking about um an artifact Knowledge Graph that we built out and we're calling guac just a couple a little introduction to myself so I'm Mike Lieberman I'm a CTO and founder co-founder of kusari supply chain security startup and I do a lot of work with the cncf I'm a security tag lead I helped co-lead the cncf secure software Factory reference architecture as well as a maintainer on Fresca an openssf project and the IMEI High I was I joined we can identify which are binaries artifacts which are container Docker container artifacts and so on so now let's look let's explore the kubernetes container I am expanding this query so I'm taking a package where the Pearl contains kubernetes controllers manager and I'm returning

### Excerpt da transcript

all right so uh we're going to be talking about um an artifact Knowledge Graph that we built out and we're calling guac just a couple a little introduction to myself so I'm Mike Lieberman I'm a CTO and founder co-founder of kusari supply chain security startup and I do a lot of work with the cncf I'm a security tag lead I helped co-lead the cncf secure software Factory reference architecture as well as a maintainer on Fresca an openssf project and the IMEI High I was I joined Google four years ago to work on tensorflow security and this year I joined the Google open source security team and started working on work and other projects right there um so we first want to just shout out that uh this tool that we're going to be showing off is an industry collaboration um you know it started off as a collaboration uh between Google kusari Purdue University and City all right so what's the problem right what's the problem here that we're trying to solve well you know um there's all this stuff that's happening in your software supply chain right you know you keep hearing about hey I need I need to be generating salsa I need to be consuming salsa I need to be generating s-bombs I need to be making sure that everybody else has s-bombs I need to be analyzing those s-bombs and all that great stuff right but one of the big problems that people keep bringing up is okay well how do I know if something has an s-bomb how do I know if it's been consumed already by you know this stuff where do I you know if if there is an s-bomb out there where should I be looking for it right um some of these things are stored in stuff like six stores recore some of this stuff is stored in you know rest apis uh random buckets uh in oci and all that sort of stuff and usually when you even pull down a package you know you might be pulling down a salsa attestation for that particular package but what about its dependencies you're not pulling information down there and like this is similar to some of the stuff we saw with for example log4j where it was um the compromised versions of log4j were really deep in your supply chain right where you thought no I'm not using log4j but it turns out you're relying on some Library which relies on some Library which relies on some library that does use a compromised uh version of that and so once you've got into go two or three layers in as you can kind of see there in the red it's like I don't know am I pulling stuff in does it exist I have no idea okay so
