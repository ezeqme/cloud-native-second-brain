---
type: session
event: "Observability Day 2025 - Europe"
year: 2025
kind: session
youtube_url: "https://www.youtube.com/watch?v=ymzn-JUtR6k"
youtube_id: "ymzn-JUtR6k"
playlist: "Observability Day 2025 - Europe"
playlist_id: "PLj6h78yzYM2O7PaLWCNCE5wKhzmzF4b6A"
playlist_index: 10
speakers: ["Vincent Boulineau"]
topics: ["Collectors", "Metrics", "Tracing", "Profiling", "SLOs", "Kubernetes", "AI Observability", "Security"]
keywords: ["container", "agent", "collector", "kubernetes", "solution", "security", "prometheus", "metric", "profile", "pod", "zero", "metrics", "gateway", "actually", "application", "information", "typically", "directly", "useful", "single", "working", "observability", "normally", "granularity"]
transcript_file: "_sources/transcripts/youtube-playlists/observability-day-2025-europe/lightning-talk-who-are-you-solving-the-container-id-resolution-with-cgroupv2/ymzn-JUtR6k.txt"
transcript_chars: 8743
status: "transcript-downloaded"
match_score: 1.08
---

# Lightning Talk: Who Are You? Solving the Container ID Resolution With Cgroupv2 - Vincent Boulineau

## Metadata

- YouTube: https://www.youtube.com/watch?v=ymzn-JUtR6k
- Playlist: Observability Day 2025 - Europe
- Speakers: Vincent Boulineau
- Topics: [[Collectors]], [[Metrics]], [[Tracing]], [[Profiling]], [[SLOs]], [[Kubernetes]], [[AI Observability]], [[Security]]

## Transcript

So I've been working for at about container monitoring for a bunch of time now and today we're going to talk about uh solving the container solution uh with CV v2. Uh so uh first let's have a look at uh the problem we are trying to solve. uh usually when you're submitting observability data uh there are two main flows either a pull flow um in which uh the target is known like is acquired so discovery from an API or from configuration and so you know uh your target and you know like name pro ID and things like that. This is typically the case for Prometheus or open metric endpoints. Uh and the other flow is a push flow where your agent or collector is exposing a port or socket uh and your application is going to send directly the data there typically for traces for instance. And the issue in that case is how to identify who is sending the data. And you may wonder why it's is important. Uh actually it's useful very useful because it allows the agent or the collector to automatically enrich your observability data.

uh with all this uh meta information like name, container name, container ID and so on that will allow you to filter and search in your obser platform of choice later. Uh so let's have a look at how it was uh done mostly in SQL v1. So C v1 uh you could uh in your application container uh have a look at this box file and in this file among other things uh you would see u your full uh secret path or like the full host path and in that path normally you would find a container ID. So with a good regular expression, you could just extract this information and attach it alongside your data and send it directly to your agent or collector. And the container ID is interesting uh data because it's unique and it provides the best granularity uh that we have in in containerized environments. Uh but now if we look at SQL V2 things are slightly different. Uh so SQL V2 was introduced uh a while ago but it's like starting to be default in the major distribution uh only a couple of years ago like in Ubuntu 222 uh red 9 11 and things like that um and now is widely adopted uh and if we look at uh the same file uh with a single v2 node uh what you will see is just this so it's empty there is nothing in there it's just this slash um so you may wonder Why?

Actually, it's not directly due to C v2. Uh it's due to uh sele 4.6 and that allow to virtualize the serarchy. Uh by virtualizing it allows to delegate part of your CPR to some processes and make them believe they are the root of a single PR and that is useful for like rootless containers for instance. uh and so with TL V2 comes by default private name spaces for all containers uh and thus uh all containers believe they are the root of a single PR key and that's why you have a slash uh so how do we do how do we solve this this issue well uh before diving into the solution let's have a look at the requirements we want for this solution uh the first one is we want to keep a container ID over granularity um because this is the current level of data we have and it's the best granularity we have. Uh the second is we don't want to add any privilege on the application side because it will change the security profile of these applications and is causing a lot of trouble.

We don't want to change anything on the host because that will be adding some friction at onboarding time uh to add observability. And finally uh in Kubernetes we want to be compatible with the post security standards baseline restricted uh it's mostly the same as as before but also it means that we cannot mount anything from the host in the application and if we look at the current SQL v1 what was the secret v1 solution it ticks all these boxes uh it works uh and and and ticks all that uh so the first solution uh and the most common one that we've seen in the community is to have a look at another file which is prox moon info and in that file indeed if you look at it in some paths you could be able to retrieve a container ID so is that it then is is the talk over well it will be very short talk so no um the caveat is actually it depends in some cases what you find there it's a container ID but in some other cases what you find there is like a volume ID which is the same format but cannot be tied easily to a container ID.

It depends on your container runtime and on the volumes you are mounting inside your container. Um so what do we do next? Well the second solution that we thought about uh was to add the mutating webbook. Uh so what what what how would that works? Basically this way would uh inject the pod u ID through the download API plus the container name. You would send that along your observed data to your agent or collector and at the given time normally this resolve to a single container ID. So that solve our our problem. However uh this solution has two drawbacks. The first one is obviously it only works in Kubernetes and the second one is when there is a container restart there is kind of a race between uh what you like the post you're watching to uh get these container ids and the change uh that is injected like so you don't know if it's like the new container or the old container just started that is the one is sending the data uh so it's a bit less accurate uh even though most of the time it works fine.

So we kept looking and we kept wondering uh would there be a more a better more universal way to do that. Uh and the idea we had was is there an information that could be kind of a proxy information. Okay, we don't have the container ID directly anymore, but is there an information that we can uh easily get from within the application uh and that being received by an agent on the host could be mapped back to a container ID. And the first idea we had was to use the mount namespace ID. Normally, every time you run a container, it allocates a mount name space ID for you and many of other namespaces as well. uh but this idea to be read requires uh um pra capability and we don't want we didn't want to add that as well if possible. So the solution that we came up with is this one. Uh actually if you look inside your application container at the CFS file uh this file as an IODE and if you look on on the host at the same uh at the full pass so similar that the one you were getting in CV1 in your uh prog uh FSC group file you would see that this these nodes are actually the same because it's the same actually filetory um so what's possible able to do uh is to read this data this this number uh inside your app container.

So like your instrumentation library attach it with your observ data as before but instead of being a container ID it's my node and on the agent on the coll on the collector side you need to mount the host of SS and by working uh this this pseudo file system and the directory structure you are going to be able to redesign nodes and map to a container ID by extracting uh from the path as it was done before in zero v1. uh with the same kind of regular expression the container ID from this path. Uh so for us this is kind of a silver bullet solution because it it takes all the boxes and um it works in all environments out of the box. requires for your agent or your collector to mount CFSC group but it's often already mounted uh because the CFS group is the source of truth for all container metrics like CPU uh memory and so on uh so it's less of an issue let's say uh in the end what did we actually implement well uh we don't only implement that we kept all these solutions if we are able to find a container ID we find uh we send it.

Uh if not then we send the iode in kubernetes we still send the pro ID and the container name in some cases. It's typically typically useful for runtimes that are based on VMs in which case this I note stuff cannot work because it doesn't share the same kernel. Um and then it's the receive on the receiver side uh that we perform the resolution based on the most accurate information we get. Uh in terms of implementation uh solution two can be implemented with like webbook uh and the pro informer for any agent. It works well with any kind of like gateway deployments. So not necessarily with like one agent per node or one connector per node. The session tree uh is requires to have an on each node and to mount the CFS group. Um and we do have uh implementation production implementation of those in our open source atog agent and some associated libraries uh with that. Um yeah and it's been using in pollution since early last year and it's been working uh fine.

Uh and that's it. So thank you all for attending. If you have any question feel free to come after or raise and the feedback QR code is also there. Thank you. [Music] [Applause]


## Related keywords

[[container]] [[agent]] [[collector]] [[kubernetes]] [[solution]] [[security]] [[prometheus]] [[metric]] [[profile]] [[pod]] [[zero]] [[metrics]]

## Notes

- Raw note imported from CNCF YouTube playlist. Promote durable insights to topic notes under `03-Topics/`.
