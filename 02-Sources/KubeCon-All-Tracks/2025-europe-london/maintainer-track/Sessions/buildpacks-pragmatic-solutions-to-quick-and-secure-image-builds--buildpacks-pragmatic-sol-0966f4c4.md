---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Juan Bustamante", "DBAccess", "Aidan Delaney", "Bloomberg"]
sched_url: https://kccnceu2025.sched.com/event/1tcyl/buildpacks-pragmatic-solutions-to-quick-and-secure-image-builds-juan-bustamante-dbaccess-aidan-delaney-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Buildpacks%3A+Pragmatic+Solutions+To+Quick+and+Secure+Image+Builds+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Buildpacks: Pragmatic Solutions To Quick and Secure Image Builds - Juan Bustamante, DBAccess & Aidan Delaney, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Juan Bustamante, DBAccess, Aidan Delaney, Bloomberg
- Schedule: https://kccnceu2025.sched.com/event/1tcyl/buildpacks-pragmatic-solutions-to-quick-and-secure-image-builds-juan-bustamante-dbaccess-aidan-delaney-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Buildpacks%3A+Pragmatic+Solutions+To+Quick+and+Secure+Image+Builds+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Buildpacks: Pragmatic Solutions To Quick and Secure Image Builds.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcyl/buildpacks-pragmatic-solutions-to-quick-and-secure-image-builds-juan-bustamante-dbaccess-aidan-delaney-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Buildpacks%3A+Pragmatic+Solutions+To+Quick+and+Secure+Image+Builds+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Eb9AweCazi8
- YouTube title: Buildpacks: Pragmatic Solutions To Quick and Secure Image Builds - Juan Bustamante & Aidan Delaney
- Match score: 0.888
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/buildpacks-pragmatic-solutions-to-quick-and-secure-image-builds/Eb9AweCazi8.txt
- Transcript chars: 28519
- Keywords: support, images, application, builder, production, control, platform, docker, heroku, little, language, python, layers, windows, organization, applications, environment, source

### Resumo baseado na transcript

Uh first of all, thank you very much for staying at the end of the day. So it's a pleasure for us to be here to talk a little bit about cloud native build pack project especially in how you could use it in your organization uh to quick and secure image builds to be deployed on any Kubernetes environment or OCI runtime environment. So it was really fast uh because obviously I I don't want anything going wrong during the demo but uh that's the important thing on the example. And the PTO folks, Juan demonstrated the PTO build packs using their Jammy base builder. This was something that traditionally build packs have had poor coverage of and now I think we're getting to the stage where we understand the problem and we can actually give decent mechanisms for installing operating system uh packages. So if you're into your software supply chain security area which a lot of us are these days because of various regulations um this is the highest level of software supply chain security that you can achieve under that particular um uh mechanism or that particular specification of supply chain security.

### Excerpt da transcript

Good evening everybody. Uh first of all, thank you very much for staying at the end of the day. It's been a long day for you. I know that and we appreciate a lot. So you can stay to the talk. So it's a pleasure for us to be here to talk a little bit about cloud native build pack project especially in how you could use it in your organization uh to quick and secure image builds to be deployed on any Kubernetes environment or OCI runtime environment. Uh my name is Juan Buptamante. I'm a platform maintainer at the build pack project. I also worked for the company named DB accessed and with me is the amazing Aiden Delaney which also a learning maintainer at the project and working from Bloomberg. Um a quick agenda for today is uh we we will be discussing a little bit uh like a 10 minutes about uh what buildpack is how it works. I will try to go through a few demos so you can see it in action. Then uh we will try to explain you a little bit from the three main personas we identify as the main users like end user and applications end users or build pack authors and platform operators.

Aan will talk you about a little bit benefits and stuff we have for them and we will conclude with some fast rebuilds and secure image stuff. Okay. So let's get started. Okay. So in essence uh the cloud native build pack project um allows you to transform your application source code into a production ready OCI image that can be deployed on any OCI runtime environment uh like Kubernetes or maybe your Podman or Docker instance locally whatever uh and we offer uh a reference implementation of Our the specification we also uh maintain uh these implementations are the paxi or the kaxi you can use it and uh what we do is we can take almost any programming language like go java python node rust and using this cli tool like kpac uh like pack or kpak we will produce an OCI image with a very defined and organized set of layers. It will start with the run image layer, okay, containing the operating system that you need for your application to be executed followed by the runtime layer of of I don't know your uh programming language.

For example, if you are running a Java application, maybe the JDK will be in that layer. Um then some dependencies it will contains all the things that you need to run your applications and finally the application layers we will get uh that will contain everything we get from uh building your source code. Um okay all this without needed a docker file. Okay, we d
