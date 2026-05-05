---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Evan Anderson", "Stacklok", "Inc"]
sched_url: https://kccnceu2025.sched.com/event/1txA2/making-crds-delightful-beyond-the-pitfalls-evan-anderson-stacklok-inc
youtube_search_url: https://www.youtube.com/results?search_query=Making+CRDs+Delightful%3A+Beyond+the+Pitfalls+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Making CRDs Delightful: Beyond the Pitfalls - Evan Anderson, Stacklok, Inc

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United Kingdom / London
- Speakers: Evan Anderson, Stacklok, Inc
- Schedule: https://kccnceu2025.sched.com/event/1txA2/making-crds-delightful-beyond-the-pitfalls-evan-anderson-stacklok-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Making+CRDs+Delightful%3A+Beyond+the+Pitfalls+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Making CRDs Delightful: Beyond the Pitfalls.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txA2/making-crds-delightful-beyond-the-pitfalls-evan-anderson-stacklok-inc
- YouTube search: https://www.youtube.com/results?search_query=Making+CRDs+Delightful%3A+Beyond+the+Pitfalls+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6KdywJWnYyg
- YouTube title: Making CRDs Delightful: Beyond the Pitfalls - Evan Anderson, Stacklok, Inc
- Match score: 0.837
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/making-crds-delightful-beyond-the-pitfalls/6KdywJWnYyg.txt
- Transcript chars: 30526
- Keywords: resources, little, native, sometimes, status, actually, resource, controller, values, control, create, custom, cluster, flux, working, events, probably, labels

### Resumo baseado na transcript

Um, I'm currently working at Stack Lock, but previously I've worked at VMware on the Tanu product and on Google Cloud. Um, one of the things I'm known for is being the founder of the Kative project or one of the founders of the Kative project. And in both cases, references to other Kubernetes resources can be helpful. Um and so something like a gateway class or storage class says hey when you create a persistent volume when you create a gateway use this implementation and here's the parameters to use when you create that gateway it will have a status that says It just tells the Kubernetes control plane, hey, here's a thing that should be granted. This is a Kubernetes resource, but if you're writing a controller, you should know about this.

### Excerpt da transcript

Yes, we are. Excellent. Uh, my name is Evan Anderson. Um, I'm currently working at Stack Lock, but previously I've worked at VMware on the Tanu product and on Google Cloud. Um, one of the things I'm known for is being the founder of the Kative project or one of the founders of the Kative project. Want to share the credit because it was really a big team effort. Um, so I have opinions about custom resources having been doing them since shortly after they were renamed thirdparty resources or from third party resources and um why is my clicker not working? Uh ah yes um and I drop in on various CNCF projects. So, um, I I've seen a bit of things out there, and this is largely derived from stuff I've seen and experienced, and as we go through these, um, I'm going to highlight which things are easy to just drop in and help fix on a project, and which things are stuff that you may need to talk to the maintainers to really get stuff going forward. But first of all, this is a UX talk for people who are writing Kubernetes operators.

And that's kind of a weird thing to say because Kubernetes operators aren't really known for great UX. Um, and there's lots of open source projects that don't have great UX and have still been very successful. Uh, the UX for Git, if anyone really loves it, I'm sorry, but it's bad. Um, Linux's UX is weird and mixed and you can see all the strata and layers of stuff. Why does Kubernetes matter? Well, because this is where developers hopefully are coming to actually live and work and hopefully they'll find it a friendly and welcoming place like we find CubeCon a friendly and welcoming place. Furthermore, this is where operations happen. And the worst thing when you're under stress is having to think real hard rather than having clear obvious solutions. Um, one of the things I was talking about with someone earlier today was feature flags. If you have a feature flag that says avoid bug foo, do you want that set to true or false? You have to think for a moment. So having clear interfaces for operating our systems is really important when things go wrong and when things go wrong is the time that it's most important.

So think about it all the time so that when things go wrong everyone is happy that it was quickly resolved and that there weren't mistakes that made it worse. We're going to start with a bunch of basics if you're writing a custom resource. Um, if you've never written a custom resource before, there's a bunch of tutorials out there
