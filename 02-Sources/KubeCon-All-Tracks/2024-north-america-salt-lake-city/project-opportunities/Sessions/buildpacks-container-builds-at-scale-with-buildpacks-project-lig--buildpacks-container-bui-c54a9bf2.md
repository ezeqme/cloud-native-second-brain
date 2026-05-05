---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["AI ML", "Runtime Containers", "SRE Reliability"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW8G/buildpacks-container-builds-at-scale-with-buildpacks-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Buildpacks%3A+Container+Builds+at+Scale+with+Buildpacks+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Buildpacks: Container Builds at Scale with Buildpacks | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW8G/buildpacks-container-builds-at-scale-with-buildpacks-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Buildpacks%3A+Container+Builds+at+Scale+with+Buildpacks+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Buildpacks: Container Builds at Scale with Buildpacks | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW8G/buildpacks-container-builds-at-scale-with-buildpacks-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Buildpacks%3A+Container+Builds+at+Scale+with+Buildpacks+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=f0lObSvR980
- YouTube title: Buildpacks: Container Builds at Scale with Buildpacks | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/buildpacks-container-builds-at-scale-with-buildpacks-project-lightning/f0lObSvR980.txt
- Transcript chars: 5702
- Keywords: actually, container, images, talking, source, layers, buildpacks, builds, companies, heroku, millions, application, easiest, native, turning, docker, salesforce, google

### Resumo baseado na transcript

all right we'll be talking about Cloud native build packs um and uh let's see yeah uh so build packs uh at a very high level are a way of turning your source code into container images without the need for a Docker file uh and we'll be talking about how real companies like uh Heroku Salesforce uh Google and VMware are using them to manage container images at the scale of like tens of millions uh so real quick my name is Joe cutner uh I'm an architect at

### Excerpt da transcript

all right we'll be talking about Cloud native build packs um and uh let's see yeah uh so build packs uh at a very high level are a way of turning your source code into container images without the need for a Docker file uh and we'll be talking about how real companies like uh Heroku Salesforce uh Google and VMware are using them to manage container images at the scale of like tens of millions uh so real quick my name is Joe cutner uh I'm an architect at Salesforce working on internal platform and with me is Terence Lee uh who's an architect at Heroku uh together we co-founded buildpacks about six years ago and uh now it's an incubating cncf project so what are build packs as I mentioned they're a way of turning your your source code into container images and at the end of this you get a container image that Maps logically to your application components so each of the layers will be you know representing uh source code or dependencies uh or some component of your app this is possible because uh Bill packs are designed to be application aware so once you create a build pack you can share it across many applications and take advantage of all the the logic the logic that's contained in it so developers use build packs because they're they're more efficient right and I mean that in the sense that uh they're actually uh potentially more sustainable because they don't repeat builds uh unless it's absolutely necessary do you want to talk about go ahead yeah just take oh you want me to take it away yeah okay uh yeah and so uh some things we have is uh Joe was talking about uh not repeating builds so we actually uh you know like a you you would have a bill pack for Java for Ruby uh and those Bill packs can decide when to reuse the cache uh when to uh you know bust the cach like if you're for instance adding a known module to your package Json uh you should be able to reuse your entire cache uh even though like a file system thing has changed right like none of the rest of the no modules are invalid but if you're upgrading your version node the node ABI is changed uh you actually probably want to blow away your cash because you need to recompile your native extensions there yeah so how many of you have made a change to your Docker file that was seemingly small but then all of a sudden busted every one of your cash layers and realized you have like another few minutes or hours to rebuild right like that that's fine for a single app maybe but it doesn't really scale to
