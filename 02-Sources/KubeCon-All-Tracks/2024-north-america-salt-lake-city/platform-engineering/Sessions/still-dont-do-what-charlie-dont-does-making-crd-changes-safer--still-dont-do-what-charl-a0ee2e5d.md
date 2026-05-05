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
speakers: ["Nick Young", "Isovalent"]
sched_url: https://kccncna2024.sched.com/event/1i7py/still-dont-do-what-charlie-dont-does-making-crd-changes-safer-nick-young-isovalent
youtube_search_url: https://www.youtube.com/results?search_query=Still+Don%27t+Do+What+Charlie+Don%27t+Does+-+Making+CRD+Changes+Safer+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Still Don't Do What Charlie Don't Does - Making CRD Changes Safer - Nick Young, Isovalent

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Salt Lake City
- Speakers: Nick Young, Isovalent
- Schedule: https://kccncna2024.sched.com/event/1i7py/still-dont-do-what-charlie-dont-does-making-crd-changes-safer-nick-young-isovalent
- Busca YouTube: https://www.youtube.com/results?search_query=Still+Don%27t+Do+What+Charlie+Don%27t+Does+-+Making+CRD+Changes+Safer+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Still Don't Do What Charlie Don't Does - Making CRD Changes Safer.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7py/still-dont-do-what-charlie-dont-does-making-crd-changes-safer-nick-young-isovalent
- YouTube search: https://www.youtube.com/results?search_query=Still+Don%27t+Do+What+Charlie+Don%27t+Does+-+Making+CRD+Changes+Safer+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=k8prMXQtfqY
- YouTube title: Still Don't Do What Charlie Don't Does - Making CRD Changes Safer - Nick Young, Isovalent
- Match score: 0.933
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/still-dont-do-what-charlie-dont-does-making-crd-changes-safer/k8prMXQtfqY.txt
- Transcript chars: 30343
- Keywords: changes, version, change, object, charlie, fields, breaking, string, validation, compatible, optional, behavior, awesomeness, making, versions, required, values, backwards

### Resumo baseado na transcript

good technically morning for five more minutes everybody uh I uh let's get this uh let's get this done and you can all uh go off and enjoy lunch welcome to the last day of the conference uh I am certainly have had an amazing time but I'm looking forward to being done as well um so welcome to still don't do what Charlie don't does making C changes safer this is actually the sequel to another talk that I did previously which was just called don't do what Charlie

### Excerpt da transcript

good technically morning for five more minutes everybody uh I uh let's get this uh let's get this done and you can all uh go off and enjoy lunch welcome to the last day of the conference uh I am certainly have had an amazing time but I'm looking forward to being done as well um so welcome to still don't do what Charlie don't does making C changes safer this is actually the sequel to another talk that I did previously which was just called don't do what Charlie don't does which was about API Design This one is about making API changes so uh my name is Nick Young uh I am a senior software engineer at is of valan at Cisco uh and pretty relevant I guess to be like who's this guy and why is he yelling at me about C design um so yeah I started looking into uh cids very early on in uh 2017 when they were still called third party resources um I uh we were looking at using that uh at the company I was working at at the time then when I was working on Contour uh I did a bunch of design work on the HTTP proxy resource which was a replacement for another CID the Engish rout resource uh and then I've been also been involved in gway API instance Inception at uh 2019 typo my bad it is 5 years this year it's 5 years next week since we started Gateway API um okay but so today's agenda so um uh I need to explain a little bit about how kubernetes stores objects and versioning for you to be able to get why a lot of these things are necessary uh and then walk through some C change mistakes using uh my uh poor uh sap Charlie don't uh as the storman and then give you some tips on what to do to avoid them and yes I did choose Charlie don't uh specifically because it has the letter c ID in it um but why did why did I come up with this stupidly complicated name for my talk well you can play The Simpsons uh so in uh The Simpsons there's episode where b gets a knife and has a the 10 dos and 500 don'ts of Night Safety and that book has a section that's called don't do what Donny don't does uh and so yes I have lifted that wholesale thanks to The Simpsons okay so this with that in mind this is Charlie don't uh Charlie uh is unlucky enough to work on a custom controller for kubernetes at uh bigco um yeah and he also has really bad luck and always makes the worst possible design decision uh so we all want to be not like Charlie so yeah poor Charlie so previously on Charlie don't in my previous talk uh I covered a bunch of things about API design principles I don't have time to go into th
