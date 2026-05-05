---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["Project Opportunities"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQXI/the-carvel-way-packaging-apis-stitching-together-sharp-unix-like-tools-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=The+Carvel+Way%3A+Packaging+APIs+stitching+together+sharp+Unix-like+tools+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The Carvel Way: Packaging APIs stitching together sharp Unix-like tools | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQXI/the-carvel-way-packaging-apis-stitching-together-sharp-unix-like-tools-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=The+Carvel+Way%3A+Packaging+APIs+stitching+together+sharp+Unix-like+tools+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The Carvel Way: Packaging APIs stitching together sharp Unix-like tools | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQXI/the-carvel-way-packaging-apis-stitching-together-sharp-unix-like-tools-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=The+Carvel+Way%3A+Packaging+APIs+stitching+together+sharp+Unix-like+tools+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_ic247XhM-A
- YouTube title: The Carvel Way: Packaging APIs stitching together sharp Unix-like tools | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-carvel-way-packaging-apis-stitching-together-sharp-unix-like-tools/_ic247XhM-A.txt
- Transcript chars: 7177
- Keywords: resources, basically, package, configuration, cluster, deploy, created, however, configurable, python, relocate, manage, artifacts, existing, interesting, course, application, scenarios

### Resumo baseado na transcript

okay uh so we here to talk about Carl and at its heart Carl is essentially it started off as a set of CA tools that are composable in nature and they help you manage your configuration and artifacts and deliver them to your end users reliably right so what's unique about the tool set is that uh they are built out in a Unix fashion which means that they can be composed with your existing tool sets existing tool chains right so you don't have to appro your entire

### Excerpt da transcript

okay uh so we here to talk about Carl and at its heart Carl is essentially it started off as a set of CA tools that are composable in nature and they help you manage your configuration and artifacts and deliver them to your end users reliably right so what's unique about the tool set is that uh they are built out in a Unix fashion which means that they can be composed with your existing tool sets existing tool chains right so you don't have to appro your entire workflow to benefit from bits of Carl however the interesting bit is that Carl sort of took a step further after that where it evolved into uh like a like a controller with surfaces apis which lets you define what your desired cluster state is as steps you would perform using your tools to obtain that desired cluster State and then of course you have to ship different versions of such an application to your customer right and I think like this sounds like a of hand waving right and how we thought we could make the best use of this time is uh to go over some scenarios which you might have already run into or uh see yourself running into and sharing how carille helps in these scenarios and sort of then sharing where you can find us over the next few days so uh Prine so let's let's take a look at some of those scenarios uh for example you wish an upstream artifact you were consuming was more configurable uh this artifact could be U like a hel chart or it could could also be a published release uh so basically uh we have a tool called VT that is short for VL templating Tool uh you can use V to shape your existing configuration files uh into like a more configurable uh uh configurable uh con like uh config itself slide so basically uh vtd has uh overlays which are based on python dialect itself so you can you can notice that it it looks pretty similar to python itself uh and uh since since it's a lot similar to python like it's based on python dialect you get an additional benefit that whatever comes out of it is basically a valid vble and so for example if you're using with the hel chart then uh you can you can use VT as a post rendering tool and you can make your Helm chart a little bit more configurable and uh and you get a valid vaml at the end of the day and you you use that to deploy artifacts uh so the next one is a bit of an interesting one it's actually uh a feature that helps our organization a lot so quite often you'll be shipping to customers who are in either highly regulated environments li
