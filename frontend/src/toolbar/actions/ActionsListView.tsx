import { Link } from '@posthog/lemon-ui'
import { useActions, useValues } from 'kea'
import { Spinner } from 'lib/lemon-ui/Spinner'

import { actionsLogic } from '~/toolbar/actions/actionsLogic'
import { actionsTabLogic } from '~/toolbar/actions/actionsTabLogic'
import { ActionType } from '~/types'

interface ActionsListViewProps {
    actions: ActionType[]
}

export function ActionsListView({ actions }: ActionsListViewProps): JSX.Element {
    const { allActionsLoading, searchTerm } = useValues(actionsLogic)
    const { selectAction } = useActions(actionsTabLogic)

    return (
        <div className="flex flex-col h-full overflow-y-scoll deprecated-space-y-px mb-2">
            {actions.length ? (
                actions.map((action, index) => (
                    <>
                        <Link
                            subtle
                            key={action.id}
                            onClick={() => selectAction(action.id || null)}
                            className="font-medium my-1 w-full"
                        >
                            <span className="min-w-[2rem] inline-block text-left">{index + 1}.</span>
                            <span className="flex-grow">
                                {action.name || <span className="italic text-secondary">Untitled</span>}
                            </span>
                        </Link>
                    </>
                ))
            ) : allActionsLoading ? (
                <div className="flex items-center">
                    <Spinner className="text-4xl" />
                </div>
            ) : (
                <div className="p-2">No {searchTerm.length ? 'matching ' : ''}actions found.</div>
            )}
        </div>
    )
}
