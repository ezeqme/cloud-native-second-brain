---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Sarah Christoff", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcws/project-lightning-talk-stir-to-combine-creating-porter-mixins-sarah-christoff-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Stir+to+Combine%3A+Creating+Porter+Mixins+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Stir to Combine: Creating Porter Mixins - Sarah Christoff, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Sarah Christoff, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcws/project-lightning-talk-stir-to-combine-creating-porter-mixins-sarah-christoff-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Stir+to+Combine%3A+Creating+Porter+Mixins+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Stir to Combine: Creating Porter Mixins.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcws/project-lightning-talk-stir-to-combine-creating-porter-mixins-sarah-christoff-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Stir+to+Combine%3A+Creating+Porter+Mixins+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4YVSW8UuHac
- YouTube title: Project Lightning Talk: Stir to Combine: Creating Porter Mixins - Sarah Christoff, Maintainer
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-stir-to-combine-creating-porter-mixins/4YVSW8UuHac.txt
- Transcript chars: 4948
- Keywords: porter, cluster, bundle, basically, cloudnative, allows, companies, devops, deploy, bundles, specification, variables, create, define, install, inside, version, looking

### Resumo baseado na transcript

I'm the lead maintainer on Porter and I'm here to teach you about what Porter is today. So Porter is a cloudnative tool agnostic uh open CS CNCF tool uh that is supported from maintainers from a diverse set of companies. So right now we have a bunch of different mix-ins, whether it's Terraform, whether it's Helm, Kubernetes, Open Tofu, all those things. We also have the Kubernetes operator which allows you to install Porter into your Kubernetes cluster the cloudnative way. And basically it allows you to manage installations, portter installations within your Kubernetes cluster. Um this helps you basically leverage pipelines like say you want to use Flux or Argo CD and we do have an Argo CD demo.

### Excerpt da transcript

Hi everyone, I'm Sarah Kristoff. I'm the lead maintainer on Porter and I'm here to teach you about what Porter is today. So Porter is a cloudnative tool agnostic uh open CS CNCF tool uh that is supported from maintainers from a diverse set of companies. So we have people not only from Microsoft but from different companies from across the world in the EU and the US. Uh, Porter is a sandbox project in the CNCF that was made by developers that experience the pain of what it's like to like try to run a bunch of DevOps tools at scale in large companies. Porter takes all of these disperate tools that developers kind of acquire over the time of existing at a large company and try to glue them together and Porter helps them enable best practices uh no matter the technology wrapping them into an immutable container image that allows you to deploy your application run your pipeline uh or set up your system in the way that is intended. So we build upon a uh system called cloudnative application bundles capab for short which is an open source specification that enables uh the OCI specification.

So you can check out the capab specification as well and that is under its own foundation. This is an example of a porter bundle which you'll notice is in YAML like everything else in our ecosystem. So you can use porter to pull credentials from either your local machine environment variables vault or azure key volt. Uh you can also have it read from a local file or a file on your host machine. Porter has this concept of mixins which are basically extensions of porter which explains to it how it will work with dev different devops tools and you can create your own mixin in five minutes which is an asterct. I don't know your DevOps tool, but basically what a mixin does is it pulls your own container image and it lets you specify how you should run it. So right now we have a bunch of different mix-ins, whether it's Terraform, whether it's Helm, Kubernetes, Open Tofu, all those things. Uh they're incredibly easy to build for yourself and I'd recommend you try some. We also have a spin mix in uh if you're into Firmian.

In the bundle, you define different actions such as install, uninstall, upgrade. You can create your own custom actions as well. So if you wanted such as like a plan action or a tearown action, you can define that yourself and run it. Now on the user end, you define this in the YAML and the user runs the bundle and they only run like porter install with their own
