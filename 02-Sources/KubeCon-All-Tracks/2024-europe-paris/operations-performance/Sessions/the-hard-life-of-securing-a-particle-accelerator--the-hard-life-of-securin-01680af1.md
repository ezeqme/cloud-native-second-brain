---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Antonio Nappi", "Sebastian Lopienski", "CERN"]
sched_url: https://kccnceu2024.sched.com/event/1YeOF/the-hard-life-of-securing-a-particle-accelerator-antonio-nappi-sebastian-lopienski-cern
youtube_search_url: https://www.youtube.com/results?search_query=The+Hard+Life+of+Securing+a+Particle+Accelerator+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The Hard Life of Securing a Particle Accelerator - Antonio Nappi & Sebastian Lopienski, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Antonio Nappi, Sebastian Lopienski, CERN
- Schedule: https://kccnceu2024.sched.com/event/1YeOF/the-hard-life-of-securing-a-particle-accelerator-antonio-nappi-sebastian-lopienski-cern
- Busca YouTube: https://www.youtube.com/results?search_query=The+Hard+Life+of+Securing+a+Particle+Accelerator+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The Hard Life of Securing a Particle Accelerator.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOF/the-hard-life-of-securing-a-particle-accelerator-antonio-nappi-sebastian-lopienski-cern
- YouTube search: https://www.youtube.com/results?search_query=The+Hard+Life+of+Securing+a+Particle+Accelerator+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rqDrrTKzNd8
- YouTube title: The Hard Life of Securing a Particle Accelerator - Antonio Nappi & Sebastian Lopienski, CERN
- Match score: 0.791
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-hard-life-of-securing-a-particle-accelerator/rqDrrTKzNd8.txt
- Transcript chars: 35593
- Keywords: basically, actually, infinite, perhaps, single, infrastructure, change, security, access, application, started, mentioned, course, sometimes, probably, multiple, particle, including

### Resumo baseado na transcript

hello hello everyone uh thank you for joining so nouses uh today I'm going to present the hard life of uh securing a particle accelerator I know he a catchy name and security at s is a Hot Topic and cover many many aspects today we are most mostly covering the identity and access management part uh my name is Antonio nappi as you can understand from my accent I'm Italian I work at s since 2015 um I was in charge of moving I mean my role is to and then we Mount this file in the klock through volume and volume ones unlik any kubernetes uh resource and then we specify through this cach confy file option uh where Klo should look for this config file now uh we move Klo to kubernetes

### Excerpt da transcript

hello hello everyone uh thank you for joining so nouses uh today I'm going to present the hard life of uh securing a particle accelerator I know he a catchy name and security at s is a Hot Topic and cover many many aspects today we are most mostly covering the identity and access management part uh my name is Antonio nappi as you can understand from my accent I'm Italian I work at s since 2015 um I was in charge of moving I mean my role is to basically uh provide infrastructure to host Java application useful for the daily life of CERN my role was to basically move this infrastructure from VMS to kubernetes so I started really early to work with kubernetes since 2016 and previously I was open St and python developer and my name is Sebastian wapinski as you can perhaps guess from my you know letters in my name I'm polish I work at CERN since 2001 uh now I'm the service manager of the single sign on Service uh but for many many years I was doing computer security at CERN so that's my kind of main U profile I would say and my background is software engineering so perhaps it's a a good moment to very briefly remind what CERN is although perhaps hopefully many of you do know uh so it's a European laboratory for particle physics so the slogan is accelerating science but what what well we or rather what physicists really do is they study the fundamental laws of nature uh by doing experiments with particles um and this will be actually relevant to you know the requirements to our system so I'm that's why I'm covering heat here so we operate a number of particle accelerators including the large hydron collider which is this huge machine um you can see the ring here um in the countryside around Geneva Switzerland but actually the accelerator is 100 me underground it's 27 km long so this is uh where those huge machines the particle detectors they which you can see here on the picture they um observe particle collisions and they observe perhaps new particles being created and this is where in 2012 the higs boson was discovered and this resulted in Nobel Prize uh in physics in 2013 however closer to our domain s is also the place where the web was born in 1989 so Tim berners Le who you can see here on a picture he you know designed or invented the HTTP protocol HTML language you know implemented the first browser uh and well BR well it wasn't called browser at that time and certainly the we first HTTP server so there's also some Computing part to to Ser certainly what
