---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Katrina Verey", "Apple", "Jeff Regan", "Google"]
sched_url: https://kccncna2021.sched.com/event/lUzm/customizing-kustomize-with-client-side-custom-resources-katrina-verey-apple-jeff-regan-google
youtube_search_url: https://www.youtube.com/results?search_query=Customizing+Kustomize+with+Client-Side+Custom+Resources+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Customizing Kustomize with Client-Side Custom Resources - Katrina Verey, Apple & Jeff Regan, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Katrina Verey, Apple, Jeff Regan, Google
- Schedule: https://kccncna2021.sched.com/event/lUzm/customizing-kustomize-with-client-side-custom-resources-katrina-verey-apple-jeff-regan-google
- Busca YouTube: https://www.youtube.com/results?search_query=Customizing+Kustomize+with+Client-Side+Custom+Resources+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Customizing Kustomize with Client-Side Custom Resources.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lUzm/customizing-kustomize-with-client-side-custom-resources-katrina-verey-apple-jeff-regan-google
- YouTube search: https://www.youtube.com/results?search_query=Customizing+Kustomize+with+Client-Side+Custom+Resources+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YlFUv4F5PYc
- YouTube title: Customizing Kustomize with Client-Side Custom Resources - Katrina Verey, Apple & Jeff Regan, Google
- Match score: 0.823
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/customizing-kustomize-with-client-side-custom-resources/YlFUv4F5PYc.txt
- Transcript chars: 36691
- Keywords: customize, extension, resource, resources, customized, extensions, custom, actually, function, configuration, transformer, output, customization, pipeline, fields, framework, client-side, versions

### Resumo baseado na transcript

all right good morning and welcome to our first and to your first session at kubecon uh north america 2021 in los angeles my name is archie i'm cncf ambassador from canada i will be a host track please welcome our speakers uh katrina veray uh sig lead instructor for six cli she's also software engineer at apple and we have jeff regen software stuff engineer at tesla though they are customized contributors so please welcome them at our first talk okay hello uh quick housekeeping items um at the

### Excerpt da transcript

all right good morning and welcome to our first and to your first session at kubecon uh north america 2021 in los angeles my name is archie i'm cncf ambassador from canada i will be a host track please welcome our speakers uh katrina veray uh sig lead instructor for six cli she's also software engineer at apple and we have jeff regen software stuff engineer at tesla though they are customized contributors so please welcome them at our first talk okay hello uh quick housekeeping items um at the end of the session you may raise your hand and ask you a question i will be running around with microphone and helping uh to answer the questions if you're watching us online you can also submit your questions in the q a box and we'll make sure your question is answered thank you thank you thanks for the introduction okay so i'm jeff and this is katrina we're going to talk about customizing customize with custom uh resources uh thanks to the cncf for bringing us all here to i'm really glad to be at a live event this time around uh the talk's gonna have three sections we're gonna talk about what is customized at least in the context of extending it it's not going to be an introduction then we're going to go into talking about how you would use custom client-side custom resources to do this extension and then go into the nuts and bolts of that so first let me review what customize is so we can talk about extending it it's three things uh it's a command line utility freestanding ammo editor that knows about kubernetes it is a set of go modules right and it is also a command in coupe cuddle so back in late 2009 or early 2019 late uh brian grant phil wittrock and others noticed that there were many missing features outstanding issues include cuddle that kind of centered around doing edits to the client side data either edits or creating data as opposed to what kubecuttle normally does which is edit the live cluster so we wanted to fix or provide a fix for these features but it was complicated we felt it was kind of big so we decided to do it outside of the contents of cube cuddle because we figured we'd probably throw away a few versions so this resulted in some modules which are now called by customizers there's a relatively thin cli and the same modules are called by a coupe cuddle so customizes configuration stream editor works with kubernetes yaml as i just said it's also very good with working with variants now everybody has multiple environments uh multiple clusters
