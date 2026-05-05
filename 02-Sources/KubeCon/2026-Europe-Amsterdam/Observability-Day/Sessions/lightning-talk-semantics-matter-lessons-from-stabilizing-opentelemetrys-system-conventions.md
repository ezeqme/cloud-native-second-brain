---
type: session
event: KubeCon Europe 2026 Amsterdam - Observability Day
year: 2026
kind: lightning-talk
room: "E103-105 (1st Floor)"
sched_url: https://colocatedeventseu2026.sched.com/event/2DY9R/cllightning-talk-semantics-matter-lessons-from-stabilizing-opentelemetrys-system-conventions-roger-coll-elastic
youtube_url: https://www.youtube.com/watch?v=QTfodanL74U
youtube_id: QTfodanL74U
match_score: 0.908
speakers: ["Roger Coll", "Elastic"]
topics: ["OpenTelemetry"]
status: transcript-downloaded
---

# ⚡Lightning Talk: Semantics Matter! Lessons From Stabilizing OpenTelemetry’s System Conventions - Roger Coll, Elastic

## Metadata

- Schedule: https://colocatedeventseu2026.sched.com/event/2DY9R/cllightning-talk-semantics-matter-lessons-from-stabilizing-opentelemetrys-system-conventions-roger-coll-elastic
- YouTube: https://www.youtube.com/watch?v=QTfodanL74U
- Room: E103-105 (1st Floor)
- Speakers: Roger Coll, Elastic
- Topics: [[OpenTelemetry]]

## Transcript

What I would like to share with you today are some of the lessons that we learn during the process of stabilizing the open telemetry system semantic conventions and why they matter in uh observability. So let's jump into the first lesson that couldn't be uh no other than uh learning how to breathe in and breathe out because uh naming is very hard and very time consuming. Actually we formed the system working group more than two years ago and although we are at the very end of the uh road if it's a stabilization we are just about to make the release candidate of the process name space. So the question is why did it take so long? Well uh some if sometimes it's hard enough to find common naming patterns within a single team.

Now imagine an open source repository with more than 200 contributors uh from 40 different companies all with their current existing uh infrastructure that depend on uh existing naming trying to agree on new uh semantics right and in fact the open telemetry semantic convention repository it's uh one of the of the open telemetry community with more comments per PR so the level of detail there it's insane. So what are the conventions that we try to agree on the system working group for example uh we would like to name how we should name uh the memory utilization of a server. Should we call it me use byes? Should we call it use memory? These are actual names used by some vendors. Or should we follow the open telemetry uh dot notation and separate the area from the resource being monitored from the type of data point and most importantly use a state to distinguish between the different uh states that the resource in this case the memory can be.

And the state it's very important because the dimension actually because it allows you to perform uh mathematical operations like aggregations while keeping the same uh name or the same reference. But we also uh try to define values for attributes for example for the OS type. Should we be very generalistic and just have Unix and Windows or should we actually be more specific more fine grade and provide some value to the users by having uh specialized attributes like the Linux, FreeBSD and Darby uh because they are very different uh kinds of kernel. So the lesson number two is that maths and abstractions end up uh defining your metrics. uh for example there's uh generic concepts right that apply to all operating systems that they are universal like the process identifier so we can define it as it is as process P ID but then there are some others that are um uh technology specific like for example the croups that it's a future just available on Linux right so we include the OS name as part of the attribute uh name and we do the same for metric met for metrics uh there's some general generic concepts like the memory usage that can should be able to monitor in all operating systems but then there are some others like the slab memory that this is a kernel feature and we decided to include the OS name as part of it uh you will see some uh blue numbers on each slides will bring you to the actual discussions where these semantics were were uh agreed for example In this case, it took a lot to figure out where to actually place the OS name within the structure if before the resource before uh the area etc etc.

And sometimes it's even impossible to agree on what use means. uh for example everyone uh wants to collect the CPU usage and CPU utilization but the truth is that we just made them opt in and we are only recommending to collect the CPU time and the reason is that the first two are derived metrics from the U third one and we are currently not shipping enough information for the backends to properly down sample uh those those values correctly. So by just uh recommending CPU time back ends should be able to properly uh get the down sampling. So in these cases the math was the arbiter of truth. Um yeah so if abstractions and shape your metrics then also your metrics end up shaping your tooling. By continuing with the example of the system CPU time, uh this used to be the u definition in the semantic conventions.

It used to have these two attributes CPU mode and CPU logical number. And what this means is that for each core and CPU mode in your system, you will have a CPU time data point. But the truth is that many users they don't care about the per core precision and they just care about the overall system uh CPU utilization or CPU time and that's why we made uh the CPU logical number optional. We made it recently optin but then we reviewed the uh hostmetric configuration in the collector and we saw that there was no way to actually uh enable or disable the attributes that are shipped within a metric. You could you were just able to enable or disable a metric and that uh yeah led to a new feature in the collector for all the receivers actually that it was merged just a couple of weeks ago.

So it will be just available on the latest versions that you can define now the set of attributes uh that uh basically the collector will ship with that metric. And for example in this case if you skip the CPU logical number on the on your collector configuration it will be automatically aggregated over all the other attributes. So in other words, you will have the overall uh system CPU time by three. All right. Um and then semantic changes and tooling changes uh they are not only code changes, they actually have an impact on the user experience. And let me show you a real example. This used to be the uh formula for uh calculating the memory utilization within a Linux server for many many years. It was total minus three maxers.

Those were values provided by the Linux kernel and a few months ago we changed it uh to this one instead in the semantic conventions and also we made the change in the collector and when users started adopting it four to five minutes months ago they saw an increase of a 7% on the reported value of the new uh formula compared to the old one. So it seemed like suddenly all their servers they were consuming 7% more of uh memory but the truth is that this is not a bug that's actually a more accurate uh reflection of reality. So hopefully with these semantic changes we provide better alerting and better resource planning in the end. And also what's very important is uh how uh do we provide a smooth user experience given this constantly uh changing ecosystem with new names, new metrics, new attributes, new formulas and that it's going to keep evolving because um stabilization is just a milestone, right?

So at elastic what we embrace is um basically versioned dashboards and by having um this version integrations we can perform breaking changes in our dashboards while making sure we don't break our current uh users view and always they can roll back to previous versions of the dashboards if they haven't changed uh or updated their infrastructure yet. And finally, uh while naming takes a lot of time, I still encourage all of you to keep contributing because systems can be observed in many ways that we haven't even considered yet. Just uh one week ago, uh someone contributed the Linux uh pressure metrics that they provide an insightful an incredible insightful um information whether if you need to scale in or scale out uh your servers.

and specifically for each uh resource if you need more CPU, more memory, more IO for and also for each of your tasks and we are already working on adding them into the conventions to the collector and finally to our dashboards. So the final lesson basically is that uh great user experience is fueled by your contributions. And I would like just to end by uh giving a huge kudos to all the system working uh group because all that I shared is basically thanks to them and also thanks all of you for uh listening me today.

## Notes

- Raw note. Promote durable insights to topic notes under `03-Topics/`.
